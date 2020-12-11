import os
import sys

from pattern.en import conjugate

from templates import (
    add_type_template,
    type_template,
    types_file_template,
    actions_file_template,
    action_template,
    reducer_case_template,
    reducers_file_template
)

from utils import (
    convert_camel_case,
    convert_reverse_camel_case,
    convert_const_case,
    create_folder,
    log_title,
    log_subtitle,
    log,
    get_filename
)


print log_title("Redux types and actions generator")

description_folder = sys.argv[1]
create_folder('output')
for file_name in os.listdir(description_folder):
    file_name = os.path.join(description_folder, file_name)
    print log_subtitle("Processing {file_name}".format(
        file_name=file_name))
    with open(file_name) as file:
        types = ''
        actions = ''
        cases = ''
        flow_types = []
        row_count = 0
        for row in file:
            row_count += 1
            if row_count == 1:
                singular_managed_type = row
                splitted_singular_managed_type = singular_managed_type.split()
                singular_managed_type_const_cased = convert_const_case(
                    splitted_singular_managed_type
                )
                singular_managed_type_camel_cased = convert_camel_case(
                    splitted_singular_managed_type
                )
                singular_managed_type_upper_camel_cased = convert_camel_case(
                    splitted_singular_managed_type,
                    capitalize_first=True
                )
                continue

            if row_count == 2:
                plural_managed_type = row
                splitted_plural_managed_type = plural_managed_type.split()
                plural_managed_type_const_cased = convert_const_case(
                    splitted_plural_managed_type
                )
                plural_managed_type_camel_cased = convert_camel_case(
                    splitted_plural_managed_type
                )
                plural_managed_type_upper_camel_cased = convert_camel_case(
                    splitted_plural_managed_type,
                    capitalize_first=True,
                )
                continue

            if row_count == 3:
                domain_name = row
                splitted_domain_name = domain_name.split()
                domain_name_camel_cased = convert_camel_case(
                    splitted_domain_name
                )
                domain_name_upper_camel_cased = convert_camel_case(
                    splitted_domain_name,
                    capitalize_first=True,
                )
                domain_name_const_cased = convert_const_case(
                    splitted_domain_name
                )
                continue

            splitted_row = row.strip().split(';')
            modification = []
            if len(splitted_row) == 2:
                noun, verb = splitted_row
            elif len(splitted_row) == 3:
                noun, verb, modification = splitted_row
                modification = [modification.strip()]
            else:
                print "Error: row with bad format."

            verb = verb.lower().strip()
            noun = noun.lower().strip().split()

            perfect_past = verb
            if verb not in ['fetch']:
                perfect_past = conjugate(verb,
                    tense='past',
                    person=3,
                    number='singular',
                    mood='indicative',
                    aspect='progressive'
                ).strip()

            imperative = conjugate(verb, 
                tense='present',
                person=2,
                number='singular',
                mood='indicative',
                aspect='imperfective',
                negated=False).strip()

            type_value = convert_const_case(
                noun +
                perfect_past.split() +
                modification)
            type_name = '{0}_TYPE'.format(type_value)
            action_name = convert_reverse_camel_case(
                imperative.split()[::-1] +
                noun +
                modification)
            flow_types.append(type_name)

            types += type_template.format(
                type_name=type_name,
                type_value=type_value
            )
            actions += action_template.format(
                action_name=action_name,
                type_name=type_name,
                type_value=type_value)
            cases += reducer_case_template.format(
                type_value=type_value
            )

    print log("CREATED: {domain_name_camel_cased} types".format(
        domain_name_camel_cased=domain_name_camel_cased
    ))
    create_folder('output/types')
    types_file_name = 'output/types/{domain_name_camel_cased}.js'.format(
        domain_name_camel_cased=domain_name_camel_cased
    )
    with open(types_file_name, 'w') as types_file:
        types_file.write(
            types_file_template.format(
                managed_type=singular_managed_type_const_cased,
                main_action_type_name=domain_name_const_cased,
                types=types,
                or_type='\n  | '.join(flow_types)
            )
        )

    print log("CREATED: {domain_name_camel_cased} actions".format(
        domain_name_camel_cased=domain_name_camel_cased
    ))
    create_folder('output/actions')
    actions_file_name = 'output/actions/{domain_name_camel_cased}.js'.format(
        domain_name_camel_cased=domain_name_camel_cased
    )
    with open(actions_file_name, 'w') as actions_file:
        actions_file.write(
            actions_file_template.format(
                types_filename=domain_name_camel_cased,
                managed_type=singular_managed_type_const_cased,
                flow_types=',\n'.join([
                    '  {0}'.format(flow_type) for flow_type in flow_types
                ]),
                actions=actions
            ))

    print log("CREATED: {domain_name_camel_cased} reducers".format(
        domain_name_camel_cased=domain_name_camel_cased)
    )
    create_folder('output/reducers')
    reducer_file_name = 'output/reducers/{domain_name_camel_cased}.js'.format(
        domain_name_camel_cased=domain_name_camel_cased
    )
    with open(reducer_file_name, 'w') as reducers_file:
        reducers_file.write(
            reducers_file_template.format(
                managed_type=singular_managed_type_const_cased,
                types_filename=domain_name_camel_cased,
                domain_state_type='{}State'.format(domain_name_upper_camel_cased),
                reducer_name=domain_name_camel_cased,
                reducer_filename=domain_name_camel_cased,
                singular_managed_type_upper_camel_cased=singular_managed_type_upper_camel_cased,
                plural_managed_type_upper_camel_cased=plural_managed_type_upper_camel_cased,
                main_action_type_name=domain_name_const_cased,
                cases=cases
            ))

    print log(
        "SUCCES: {domain_name_camel_cased}".format(
            domain_name_camel_cased=domain_name_camel_cased
        ),
        code='okblue'
    )
print log("SUCCES: process complete", code='okgreen')
