type_template = '''export const {type_value} = '{type_value}';

'''

types_file_template = ''''''

action_template = '''export const {action_name} = () => ({{
  type: types.{type_value},
  payload: {{}},
}});

'''

actions_file_template = '''import * as types from '../types/{domain}';


{actions}
'''

reducer_case_template = '''
  case types.{type_value}: {{
    return state;
  }}
'''

reducers_file_template = '''import {{ combineReducers }} from 'redux';

import * as common from './common';
import * as types from '../types/{domain}';

const byId = common.byId({{
  added: [],
  updated: [],
  updatedInBulk: [],
  fetched: [],
  removed: [],
  confirmed: [],
  addedToArrayAttribute: [],
  removedFromArrayAttribute: [],
  replacedInArrayAttribute: [],
  cascade: {{}},
  defaultAttributes: {{}},
}});

const order = common.order({{
  added: [],
  fetched: [],
  replaced: [],
  removed: [],
  confirmed: [],
}});

const fetching = common.fetching({{
  started: [],
  succeed: [],
  failed: [],
}});

const isFetching = common.isFetching({{
  started: [],
  succeed: [],
  failed: [],
}});

const error = common.error({{
  clear: [],
  populate: [],
}});

const errors = common.errors({{
  clear: [],
  populate: [],
}});

const isToggled = common.toggle({{
  turnedOn: [],
  turnedOff: [],
  default: true,
}});

const selected = common.mux({{
  selected: [],
  allDeselected: [],
  default: -1,
}});

const counter = common.counter({{
  incremented: [],
  decremented: [],
  reset: [],
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
  counter,
}});


export default {domain};


// Selectors
export const get{singular_upper_camel_domain} = (state, id) => state.byId[id];
export const get{upper_camel_domain} = state => state.order.map(i => get{singular_upper_camel_domain}(state, i));
export const is{singular_upper_camel_domain}Fetching = (state, id) => state.fetching.includes(id);
export const isFetching{upper_camel_domain} = state => state.isFetching;
export const get{upper_camel_domain}Error = state => state.error;
export const get{singular_upper_camel_domain}Error = (state, id => state.errors[id];
export const are{upper_camel_domain}Toggled = state => state.toggle;
export const getSelected{singular_upper_camel_domain} = state => get{singular_upper_camel_domain}(state, state.selected);
export const get{singular_upper_camel_domain}Counter = state: number => state.counter;

//////////////////////////////////////////////////////////////
// TODO: move to index.js
//////////////////////////////////////////////////////////////

// Imports
import {domain}, * as from{upper_camel_domain} from './{domain}';

// Reducer
const reducer = combineReducers({{
  {domain}
}});

// Bottom
export const get{singular_upper_camel_domain} = genSelector(from{upper_camel_domain}.get{singular_upper_camel_domain}, '{domain}');
export const get{upper_camel_domain} = genSelector(from{upper_camel_domain}.get{upper_camel_domain}, '{domain}');
export const is{singular_upper_camel_domain}Fetching = genSelector(from{upper_camel_domain}.is{singular_upper_camel_domain}Fetching, '{domain}');
export const isFetching{upper_camel_domain} = genSelector(from{upper_camel_domain}.isFetching{upper_camel_domain}, '{domain}');
export const get{upper_camel_domain}Error = genSelector(from{upper_camel_domain}.get{upper_camel_domain}Error, '{domain}');
export const get{singular_upper_camel_domain}Error = genSelector(from{upper_camel_domain}.get{singular_upper_camel_domain}Error, '{domain}');
export const are{upper_camel_domain}Toggled = genSelector(from{upper_camel_domain}.are{upper_camel_domain}Toggled, '{domain}');
export const getSelected{singular_upper_camel_domain} = genSelector(from{upper_camel_domain}.getSelected{singular_upper_camel_domain}, '{domain}');
export const get{singular_upper_camel_domain}Counter = genSelector(from{upper_camel_domain}.get{singular_upper_camel_domain}Counter, '{domain}');

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
