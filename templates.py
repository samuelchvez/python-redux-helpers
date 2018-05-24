domain_type_template = '{domain}_TYPE'

type_template = '''export type {type_name} = {{
  type: '{type_value}',
  payload: {{}}
}};
export const {type_value} = '{type_value}';

'''

types_file_template = '''// @flow
export type {domain_type} = {{}};

{types}export type {domain}_ACTION_TYPE =
  | {or_type};
'''

action_template = '''export const {action_name} = (): {type_name} => ({{
  type: types.{type_value},
  payload: {{}}
}});

'''

actions_file_template = '''// @flow
import * as types from '../types/{domain}';
import type {{
{flow_types}
}} from '../types/{domain}';

{actions}
'''

reducer_case_template = '''
  case types.{type_value}: {{
    return state;
  }}
'''

reducers_file_template = '''//@flow
import {{ combineReducers }} from 'redux';

import type {{ ID_TYPE, ERROR_TYPE }} from '../types/common';
import type {{ {domain_type} }} from '../types/{domain}';
import * as common from './common';
import * as types from '../types/{domain}';

export type {domain_state_type} = {{
  byId: {{ [ID_TYPE]: {domain_type} }},
  order: Array<ID_TYPE>,
  fetching: Array<ID_TYPE>,
  isFetching: boolean,
  error: ERROR_TYPE,
  errors: {{ [ID_TYPE]: ERROR_TYPE }},
  isToggled: boolean,
  selected: number,
  counter: number
}};

const byId = common.byId({{
  added: [],
  updated: [],
  fetched: [],
  removed: [],
  confirmed: [],
  addedToArrayAttribute: [],
  removedFromArrayAttribute: [],
  defaultAttributes: {{}}
}});

const order = common.order({{
  added: [],
  fetched: [],
  removed: [],
}});

const fetching = common.fetching({{
  started: [],
  succeed: [],
  failed: []
}});

const isFetching = common.isFetching({{
  started: [],
  succeed: [],
  failed: []
}});

const error = common.error({{
  clear: [],
  populate: []
}});

const errors = common.errors({{
  clear: [],
  populate: []
}});

const isToggled = common.toggle({{
  turnedOn: [],
  turnedOff: [],
  default: true
}});

const selected = common.mux({{
  selected: [],
  allDeselected: [],
  default: -1
}});

const counter = common.counter({{
  incremented: [],
  decremented: [],
  reset: []
}});

const {domain} = combineReducers({{
  byId,
  order,
  fetching,
  isFetching,
  error,
  errors,
  isToggled,
  mux,
  counter
}});


export default {domain};


// Selectors
export const get{singular_upper_camel_domain} = (state: {domain_state_type}, id: ID_TYPE): ?{domain_type} => state.byId[id];
export const get{upper_camel_domain} = (state: {domain_state_type}): Array<{domain_type}> => state.order.map(i => get{singular_upper_camel_domain}(state, i));
export const is{singular_upper_camel_domain}Fetching = (state: {domain_state_type}, id: ID_TYPE): boolean => state.fetching.includes(id);
export const isFetching{upper_camel_domain} = (state: {domain_state_type}): boolean => state.isFetching;
export const get{upper_camel_domain}Error = (state: {domain_state_type}): ERROR_TYPE => state.error;
export const get{singular_upper_camel_domain}Error = (state: {domain_state_type}, id: ID_TYPE): ERROR_TYPE => state.errors[id];
export const are{upper_camel_domain}Toggled = (state: {domain_state_type}): boolean => state.toggle;
export const getSelected{singular_upper_camel_domain} = (state: {domain_state_type}): ?{domain_type} => get{singular_upper_camel_domain}(state, state.selected);
export const get{singular_upper_camel_domain}Counter = (state: {domain_state_type}): number => state.counter;

/*
const {domain} =  (
  state: {domain_state_type} = {{}},
  action: {main_type}): {domain_state_type} => {{
  switch (action.type) {{
    {cases}
    default:
      return state;
  }}
}}
*/

'''
