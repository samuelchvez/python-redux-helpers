add_type_template = '{to_type}_TYPE'

type_template = '''export type {type_name} = {{
  type: '{type_value}',
  payload: {{}},
}};
export const {type_value} = '{type_value}';

'''

types_file_template = '''// @flow
import type {{ ID_TYPE, ERROR_TYPE }} from './common';

export type {managed_type} = {{}};

{types}export type {main_action_type_name}_ACTION_TYPE =
  | {or_type};
'''

action_template = '''export const {action_name} = (): {type_name} => ({{
  type: types.{type_value},
  payload: {{}},
}});

'''

actions_file_template = '''// @flow
import type {{ ID_TYPE, ERROR_TYPE }} from '../types/common';

import type {{
  {managed_type},
{flow_types},
}} from '../types/{types_filename}';
import * as types from '../types/{types_filename}';


{actions}'''

reducer_case_template = '''
  case types.{type_value}: {{
    return state;
  }}
'''

reducers_file_template = '''// @flow
import {{ combineReducers }} from 'redux';

import type {{ ID_TYPE, ERROR_TYPE }} from '../types/common';
import type {{ {managed_type} }} from '../types/{types_filename}';
import type {{ SubstateMultiplexerStateType }} from './common/substateMultiplexer';
import * as common from './common';
import * as types from '../types/{types_filename}';

export type {domain_state_type} = {{
  byId: {{ [ID_TYPE]: {managed_type} }},
  order: Array<ID_TYPE>,
  fetching: Array<ID_TYPE>,
  isFetching: boolean,
  error: ERROR_TYPE,
  errors: {{ [ID_TYPE]: ERROR_TYPE }},
  isToggled: boolean,
  selected: number,
  counter: number,
  substateMultiplexer: SubstateMultiplexerStateType,
  orderById: {{ [ID_TYPE]: Array<ID_TYPE> }},
  timestamp: number,
  nextPage: ?number,
  keyExtractorById: {{ [ID_TYPE]: mixed }},
  singleton: Object,
}};

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

const selected = common.selected({{
  selected: [],
  allDeselected: [],
  default: -1,
}});

const counter = common.counter({{
  incremented: [],
  decremented: [],
  reset: [],
}});

const substateMultiplexer = common.substateMultiplexer({{
  added: [],
  fetched: [],
  replaced: [],
  removed: [],
  confirmed: [],
  selected: [],
  allDeselected: [],
}});

const orderById = common.orderById({{
  fetched: [],
  replaced: [],
  idKey: 'id',
}});

const timestamp = common.keyExtractor({{
  clear: [],
  set: [],
  extractionKey: 'timestamp',
  default: -1,
}});

const nextPage = common.keyExtractor({{
  clear: [],
  set: [],
  extractionKey: 'nextPage',
  default: 1,
}});

const keyExtractorById = common.keyExtractorById({{
  clear: [],
  set: [],
  extractionKey: 'nextPage',
  idKey: 'id',
  default: null,
}});

const singleton = common.singleton({{
  clear: [],
  populate: [],
  update: [],
}})

const {reducer_name} = combineReducers({{
  byId,
  order,
  fetching,
  isFetching,
  error,
  errors,
  isToggled,
  selected,
  counter,
  substateMultiplexer,
  orderById,
  timestamp,
  nextPage,
  keyExtractorById,
  singleton,
}});


export default {reducer_name};


// Selectors
export const get{singular_managed_type_upper_camel_cased} = (state: {domain_state_type}, id: ID_TYPE): ?{managed_type} => state.byId[id];
export const get{plural_managed_type_upper_camel_cased} = (state: {domain_state_type}): Array<?{managed_type}> => state.order.map(i => get{singular_managed_type_upper_camel_cased}(state, i));
export const is{singular_managed_type_upper_camel_cased}Fetching = (state: {domain_state_type}, id: ID_TYPE): boolean => state.fetching.includes(id);
export const isFetching{plural_managed_type_upper_camel_cased} = (state: {domain_state_type}): boolean => state.isFetching;
export const get{plural_managed_type_upper_camel_cased}Error = (state: {domain_state_type}): ERROR_TYPE => state.error;
export const get{singular_managed_type_upper_camel_cased}Error = (state: {domain_state_type}, id: ID_TYPE): ERROR_TYPE => state.errors[id];
export const are{plural_managed_type_upper_camel_cased}Toggled = (state: {domain_state_type}): boolean => state.toggle;
export const getSelected{singular_managed_type_upper_camel_cased} = (state: {domain_state_type}): ?{managed_type} => get{singular_managed_type_upper_camel_cased}(state, state.selected);
export const get{singular_managed_type_upper_camel_cased}Counter = (state: {domain_state_type}): number => state.counter;
export const getOrderFor = (state: {domain_state_type}, id: ID_TYPE): Array<ID_TYPE>? => state.orderById[id];
export const getTimestamp = (state: {domain_state_type}): number => state.timestamp;
export const getNextPage = (state: {domain_state_type}): ?number => state.nextPage;
export const getKeyExtractionFor = (state: {domain_state_type}, id: ID_TYPE): mixed => state.keyExtractorById[id];
export const getSingleton = (state: {domain_state_type}): Object => state.singleton;

//////////////////////////////////////////////////////////////
// TODO: move to index.js
//////////////////////////////////////////////////////////////

// Imports
import type {{ {domain_state_type} }} from './{reducer_filename}';
import {reducer_name}, * as from{plural_managed_type_upper_camel_cased} from './{reducer_filename}';

// AppState
export type AppState = {{
  {reducer_name}: {domain_state_type}
}};

// Reducer
const reducer = combineReducers({{
  {reducer_name}
}});

// Bottom
export const get{singular_managed_type_upper_camel_cased} = genSelector(from{plural_managed_type_upper_camel_cased}.get{singular_managed_type_upper_camel_cased}, '{reducer_name}');
export const get{plural_managed_type_upper_camel_cased} = genSelector(from{plural_managed_type_upper_camel_cased}.get{plural_managed_type_upper_camel_cased}, '{reducer_name}');
export const is{singular_managed_type_upper_camel_cased}Fetching = genSelector(from{plural_managed_type_upper_camel_cased}.is{singular_managed_type_upper_camel_cased}Fetching, '{reducer_name}');
export const isFetching{plural_managed_type_upper_camel_cased} = genSelector(from{plural_managed_type_upper_camel_cased}.isFetching{plural_managed_type_upper_camel_cased}, '{reducer_name}');
export const get{plural_managed_type_upper_camel_cased}Error = genSelector(from{plural_managed_type_upper_camel_cased}.get{plural_managed_type_upper_camel_cased}Error, '{reducer_name}');
export const get{singular_managed_type_upper_camel_cased}Error = genSelector(from{plural_managed_type_upper_camel_cased}.get{singular_managed_type_upper_camel_cased}Error, '{reducer_name}');
export const are{plural_managed_type_upper_camel_cased}Toggled = genSelector(from{plural_managed_type_upper_camel_cased}.are{plural_managed_type_upper_camel_cased}Toggled, '{reducer_name}');
export const getSelected{singular_managed_type_upper_camel_cased} = genSelector(from{plural_managed_type_upper_camel_cased}.getSelected{singular_managed_type_upper_camel_cased}, '{reducer_name}');
export const get{singular_managed_type_upper_camel_cased}Counter = genSelector(from{plural_managed_type_upper_camel_cased}.get{singular_managed_type_upper_camel_cased}Counter, '{reducer_name}');
export const getSingleton = genSelector(from{plural_managed_type_upper_camel_cased}.getSingleton, '{reducer_name}');

/*
const {reducer_name} =  (
  state: {domain_state_type} = {{}},
  action: {main_action_type_name}): {domain_state_type} => {{
  switch (action.type) {{
    {cases}
    default:
      return state;
  }}
}}
*/
'''
