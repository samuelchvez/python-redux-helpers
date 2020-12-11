add_type_template = '{to_type}_TYPE'

type_template = '''export const {type_value} = '{type_value}';

'''

types_file_template = '''{types}'''

action_template = '''export const {action_name} = () => ({{
  type: types.{type_value},
  payload: {{}},
}});

'''

actions_file_template = '''import * as types from '../types/{types_filename}';


{actions}'''

reducer_case_template = '''
  case types.{type_value}: {{
    return state;
  }}
'''

reducers_file_template = '''import {{ combineReducers }} from 'redux';

import * as common from './common';
import * as types from '../types/{types_filename}';

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
export const get{singular_managed_type_upper_camel_cased} = (state, id) => state.byId[id];
export const get{plural_managed_type_upper_camel_cased} = state => state.order.map(i => get{singular_managed_type_upper_camel_cased}(state, i));
export const is{singular_managed_type_upper_camel_cased}Fetching = (state, id) => state.fetching.includes(id);
export const isFetching{plural_managed_type_upper_camel_cased} = state => state.isFetching;
export const get{plural_managed_type_upper_camel_cased}Error = state => state.error;
export const get{singular_managed_type_upper_camel_cased}Error = (state, id) => state.errors[id];
export const are{plural_managed_type_upper_camel_cased}Toggled = state => state.toggle;
export const getSelected{singular_managed_type_upper_camel_cased} = state => get{singular_managed_type_upper_camel_cased}(state, state.selected);
export const get{singular_managed_type_upper_camel_cased}Counter = state => state.counter;
export const getOrderFor = (state, id) => state.orderById[id];
export const getTimestamp = state => state.timestamp;
export const getNextPage = state => state.nextPage;
export const getKeyExtractionFor = (state, id) => state.keyExtractorById[id];
export const getSingleton = state => state.singleton;

//////////////////////////////////////////////////////////////
// TODO: move to index.js
//////////////////////////////////////////////////////////////

// Imports
import {reducer_name}, * as from{plural_managed_type_upper_camel_cased} from './{reducer_filename}';


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
  state = {{}},
  action,
) => {{
  switch (action.type) {{
    {cases}
    default:
      return state;
  }}
}}
*/
'''
