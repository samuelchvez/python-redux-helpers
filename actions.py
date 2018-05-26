import os
import sys

from pattern.en import conjugate

from templates import (
    domain_type_template,
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
    singularize,
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
        for row in file:
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

    domain = get_filename(file.name)
    singular_domain = singularize(domain)
    upper_domain = domain.upper()
    singular_upper_domain = singularize(upper_domain)
    upper_camel_domain = convert_camel_case(domain.split())
    singular_upper_camel_domain = singularize(upper_camel_domain)
    domain_type = domain_type_template.format(domain=singular_upper_domain)
    domain_state_type = '{0}State'.format(upper_camel_domain)

    print log("CREATED: {domain} types".format(domain=domain))
    create_folder('output/types')
    types_file_name = 'output/types/{domain}.js'.format(domain=domain)
    with open(types_file_name, 'w') as types_file:
        types_file.write(
            types_file_template.format(
                upper_camel_domain=upper_camel_domain,
                domain_type=domain_type,
                domain=upper_domain,
                types=types,
                or_type='\n  | '.join(flow_types)
            )
        )

    print log("CREATED: {domain} actions".format(domain=domain))
    create_folder('output/actions')
    actions_file_name = 'output/actions/{domain}.js'.format(domain=domain)
    with open(actions_file_name, 'w') as actions_file:
        actions_file.write(
            actions_file_template.format(
                domain=domain,
                domain_type=domain_type,
                flow_types=',\n'.join([
                    '  {0}'.format(flow_type) for flow_type in flow_types
                ]),
                actions=actions
            ))

    print log("CREATED: {domain} reducers".format(domain=domain))
    create_folder('output/reducers')
    reducer_file_name = 'output/reducers/{domain}.js'.format(domain=domain)
    with open(reducer_file_name, 'w') as reducers_file:
        reducers_file.write(
            reducers_file_template.format(
                domain=domain,
                domain_type=domain_type,
                upper_camel_domain=upper_camel_domain,
                singular_upper_camel_domain=singular_upper_camel_domain,
                main_type='{0}_ACTION_TYPE'.format(domain.upper()),
                domain_state_type=domain_state_type,
                cases=cases
            ))

    print log("SUCCES: {domain}".format(domain=domain), code='okblue')
print log("SUCCES: process complete", code='okgreen')
