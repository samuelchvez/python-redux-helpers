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
