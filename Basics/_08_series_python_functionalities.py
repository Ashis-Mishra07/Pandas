import pandas as pd

# len/type/dir/sorted/max/min
len(subs)  # return u the length of the subs
type(subs) # retunr u the type i.e. Series 
dir(subs)  # return u all the functions that can be applied on the series
sorted(subs) # sort it and store in list ( so generally not used)
min(subs)  # return the min value
max(subs)  # return the max value

'''
The output will be:

365
<class 'pandas.core.series.Series'>
['T', '_AXIS_LEN', '_AXIS_ORDERS', '_AXIS_REVERSED', '_AXIS_TO_AXIS_NUMBER', '_HANDLED_TYPES', '__abs__', '__add__', '__and__', '__annotations__', '__array__', '__array_priority__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__divmod__', '__doc__', '__eq__', '__finalize__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__imod__', '__imul__', '__init__', '__init_subclass__', '__int__', '__invert__', '__ior__', '__ipow__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__long__', '__lt__', '__matmul__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__weakref__', '__xor__', '_accessors', '_accum_func', '_add_numeric_operations', '_agg_by_level', '_agg_examples_doc', '_agg_see_also_doc', '_align_frame', '_align_series', '_arith_method', '_as_manager', '_attrs', '_binop', '_can_hold_na', '_check_inplace_and_allows_duplicate_labels', '_check_inplace_setting', '_check_is_chained_assignment_possible', '_check_label_or_level_ambiguity', '_check_setitem_copy', '_clear_item_cache', '_clip_with_one_bound', '_clip_with_scalar', '_cmp_method', '_consolidate', '_consolidate_inplace', '_construct_axes_dict', '_construct_axes_from_arguments', '_construct_result', '_constructor', '_constructor_expanddim', '_convert', '_convert_dtypes', '_data', '_dir_additions', '_dir_deletions', '_drop_axis', '_drop_labels_or_levels', '_duplicated', '_find_valid_index', '_flags', '_from_mgr', '_get_axis', '_get_axis_name', '_get_axis_number', '_get_axis_resolvers', '_get_block_manager_axis', '_get_bool_data', '_get_cacher', '_get_cleaned_column_resolvers', '_get_index_resolvers', '_get_label_or_level_values', '_get_numeric_data', '_get_value', '_get_values', '_get_values_tuple', '_get_with', '_gotitem', '_hidden_attrs', '_index', '_indexed_same', '_info_axis', '_info_axis_name', '_info_axis_number', '_init_dict', '_init_mgr', '_inplace_method', '_internal_names', '_internal_names_set', '_is_cached', '_is_copy', '_is_label_or_level_reference', '_is_label_reference', '_is_level_reference', '_is_mixed_type', '_is_view', '_item_cache', '_ixs', '_logical_func', '_logical_method', '_map_values', '_maybe_update_cacher', '_memory_usage', '_metadata', '_mgr', '_min_count_stat_function', '_name', '_needs_reindex_multi', '_protect_consolidate', '_reduce', '_reindex_axes', '_reindex_indexer', '_reindex_multi', '_reindex_with_indexers', '_replace_single', '_repr_data_resource_', '_repr_latex_', '_reset_cache', '_reset_cacher', '_set_as_cached', '_set_axis', '_set_axis_name', '_set_axis_nocheck', '_set_is_copy', '_set_labels', '_set_name', '_set_value', '_set_values', '_set_with', '_set_with_engine', '_slice', '_stat_axis', '_stat_axis_name', '_stat_axis_number', '_stat_function', '_stat_function_ddof', '_take_with_is_copy', '_typ', '_update_inplace', '_validate_dtype', '_values', '_where', 'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'append', 'apply', 'argmax', 'argmin', 'argsort', 'array', 'asfreq', 'asof', 'astype', 'at', 'at_time', 'attrs', 'autocorr', 'axes', 'backfill', 'between', 'between_time', 'bfill', 'bool', 'clip', 'combine', 'combine_first', 'compare', 'convert_dtypes', 'copy', 'corr', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'divmod', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 'dtype', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'ewm', 'expanding', 'explode', 'factorize', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'flags', 'floordiv', 'ge', 'get', 'groupby', 'gt', 'hasnans', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'interpolate', 'is_monotonic', 'is_monotonic_decreasing', 'is_monotonic_increasing', 'is_unique', 'isin', 'isna', 'isnull', 'item', 'items', 'iteritems', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lt', 'mad', 'map', 'mask', 'max', 'mean', 'median', 'memory_usage', 'min', 'mod', 'mode', 'mul', 'multiply', 'name', 'nbytes', 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'plot', 'pop', 'pow', 'prod', 'product', 'quantile', 'radd', 'rank', 'ravel', 'rdiv', 'rdivmod', 'reindex', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'repeat', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'searchsorted', 'sem', 'set_axis', 'set_flags', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort_index', 'sort_values', 'squeeze', 'std', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_frame', 'to_hdf', 'to_json', 'to_latex', 'to_list', 'to_markdown', 'to_numpy', 'to_period', 'to_pickle', 'to_sql', 'to_string', 'to_timestamp', 'to_xarray', 'transform', 'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 'unique', 'unstack', 'update', 'value_counts', 'values', 'var', 'view', 'where', 'xs']
[33, 33, 35, 37, 39, 40, 40, 40, 40, 42, 42, 43, 44, 44, 44, 45, 46, 46, 48, 49, 49, 49, 49, 50, 50, 50, 51, 54, 56, 56, 56, 56, 57, 61, 62, 64, 65, 65, 66, 66, 66, 66, 67, 68, 70, 70, 70, 71, 71, 72, 72, 72, 72, 72, 73, 74, 74, 75, 76, 76, 76, 76, 77, 77, 78, 78, 78, 79, 79, 80, 80, 80, 81, 81, 82, 82, 83, 83, 83, 84, 84, 84, 85, 86, 86, 86, 87, 87, 87, 87, 88, 88, 88, 88, 88, 89, 89, 89, 90, 90, 90, 90, 91, 92, 92, 92, 93, 93, 93, 93, 95, 95, 96, 96, 96, 96, 97, 97, 98, 98, 99, 99, 100, 100, 100, 101, 101, 101, 102, 102, 103, 103, 104, 104, 104, 105, 105, 105, 105, 105, 105, 105, 105, 105, 108, 108, 108, 108, 108, 108, 109, 109, 110, 110, 110, 111, 111, 112, 113, 113, 113, 114, 114, 114, 114, 115, 115, 115, 115, 117, 117, 117, 118, 118, 119, 119, 119, 119, 120, 122, 123, 123, 123, 123, 123, 124, 125, 126, 127, 128, 128, 129, 130, 131, 131, 132, 132, 134, 134, 134, 135, 135, 136, 136, 136, 137, 138, 138, 138, 139, 140, 144, 145, 146, 146, 146, 146, 147, 149, 150, 150, 150, 150, 151, 152, 152, 152, 153, 153, 153, 154, 154, 154, 155, 155, 156, 156, 156, 156, 157, 157, 157, 157, 158, 158, 159, 159, 160, 160, 160, 160, 162, 164, 166, 167, 167, 168, 170, 170, 170, 170, 171, 172, 172, 173, 173, 173, 174, 174, 175, 175, 176, 176, 177, 178, 179, 179, 180, 180, 180, 182, 183, 183, 183, 184, 184, 184, 185, 185, 185, 185, 186, 186, 186, 188, 189, 190, 190, 192, 192, 192, 196, 196, 196, 197, 197, 202, 202, 202, 203, 204, 206, 207, 209, 210, 210, 211, 212, 213, 214, 216, 219, 220, 221, 221, 222, 222, 224, 225, 225, 226, 227, 228, 229, 230, 231, 233, 236, 236, 237, 241, 243, 244, 245, 247, 249, 254, 254, 258, 259, 259, 261, 261, 265, 267, 268, 269, 276, 276, 290, 295, 301, 306, 312, 396]
33
396

'''


# Type Conversion
list(marks_series) # series converted into list
'''
The output
[67, 100, 89, 100, 90, 100]
'''

dict(marks_series) # series converted into dictionary
'''
The output
{
    'maths': 67,
    'phy': 100,
    'chem': 89, 
    'eng': 100, 
    'hindi': 90, 
    'evs': 100
}
'''


# membership operator
'2 States (2014 film)' in movies  # return true if the index is present in the series

'''
    By default in/not in operator checks for the index
'''
# for values check
'Alia Bhatt' in movies.values # return true if the value is present in the series




# Looping
for i in movies:
  print(i)

'''
loops runs on VALUES not on index
'''
# for on index
for i in movies.index:
  print(i)



# Arithmetic Operators(Broadcasting) 
'''
This is much more like broadcasting , adding a value to each element of the series
'''
100 + marks_series  # add 100 to each value of the series


# Relational Operators
vk >= 50   #  against each value of the series it will show false or true



# Boolean Indexing on Series

vk[vk >= 50]  # return the values which are greater than 50
vk[vk >= 50].size  # return the number of values which are greater than 50

# Count number of day when I had more than 200 subs a day
subs[subs > 200].size

# find actors who have done more than 20 movies
num_movies = movies.value_counts()  # here it will return the count of each actor
num_movies[num_movies > 20]






# Plotting Graphs

subs.plot() # plot the graph of the subscribers gained y axis -> days , x axis -> subs

movies.value_counts().head(20).plot(kind='pie')
'''
The above  , movies.value_counts() will return the count of each actor
and for top 20 actors , use head(20) 
then plot it with kind ='pie' | 'bar' 
'''

