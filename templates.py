type_template = '''export type {type_name} = {{
  type: '{type_value}';
  payload: undefined
}};
export const {type_value} = '{type_value}';

'''

types_file_template = '''// @flow
{types}export type {domain}_ACTION_TYPE =
  | {or_type};
'''

action_template = '''export const {action_name} = (): {type_name} => ({{
  type: types.{type_value},
  payload: {{}}
}});

'''

actions_file_template = '''// @flow
import * as types from '..types/{domain}';
import type {{
{flow_types}
}} from '..types/{domain}';

{actions}
'''

reducer_case_template = '''
  case types.{type_value}: {{
    return state;
  }}
''';

reducers_file_template = '''//@flow
import {{ combineReducers }} from 'redux';

import * as types from '../types/{domain}';
import type {{{main_type}}} from '../types/{domain}';

export type {domain_state_type} = Object;

const {domain} =  (
  state: {domain_state_type} = {{}},
  action: {main_type}): {domain_state_type} => {{
  switch (action.type) {{
    {cases}
    default:
      return state;
  }}
}}

export default {domain};
''';
