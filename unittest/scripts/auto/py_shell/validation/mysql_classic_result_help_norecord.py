#@ __global__
||

#@<OUT> classicresult
NAME
      ClassicResult - Allows browsing through the result information after
                      performing an operation on the database through the MySQL
                      Protocol.

DESCRIPTION
      This class allows access to the result set from the classic MySQL data
      model to be retrieved from Dev API queries.

PROPERTIES
      affected_row_count
            The number of affected rows for the last operation.

      auto_increment_value
            Returns the last insert id auto generated (from an insert
            operation)

      column_count
            Retrieves the number of columns on the current result.

      column_names
            Gets the columns on the current result.

      columns
            Gets the column metadata for the columns on the active result.

      execution_time
            Retrieves a string value indicating the execution time of the
            executed operation.

      info
            Retrieves a string providing information about the most recently
            executed statement.

      warning_count
            The number of warnings produced by the last statement execution.

      warnings
            Retrieves the warnings generated by the executed operation.

FUNCTIONS
      fetch_all()
            Returns a list of Row objects which contains an element for every
            record left on the result.

      fetch_one()
            Retrieves the next Row on the ClassicResult.

      get_affected_row_count()
            The number of affected rows for the last operation.

      get_auto_increment_value()
            Returns the last insert id auto generated (from an insert
            operation)

      get_column_count()
            Retrieves the number of columns on the current result.

      get_column_names()
            Gets the columns on the current result.

      get_columns()
            Gets the column metadata for the columns on the active result.

      get_execution_time()
            Retrieves a string value indicating the execution time of the
            executed operation.

      get_info()
            Retrieves a string providing information about the most recently
            executed statement.

      get_warning_count()
            The number of warnings produced by the last statement execution.

      get_warnings()
            Retrieves the warnings generated by the executed operation.

      has_data()
            Returns true if the last statement execution has a result set.

      help()
            Provides help about this class and it's members

      next_data_set()
            Prepares the SqlResult to start reading data from the next Result
            (if many results were returned).

#@<OUT> classicresult.affected_row_count
NAME
      affected_row_count - The number of affected rows for the last operation.

SYNTAX
      <ClassicResult>.affected_row_count

#@<OUT> classicresult.auto_increment_value
NAME
      auto_increment_value - Returns the last insert id auto generated (from an
                             insert operation)

SYNTAX
      <ClassicResult>.auto_increment_value

#@<OUT> classicresult.column_count
NAME
      column_count - Retrieves the number of columns on the current result.

SYNTAX
      <ClassicResult>.column_count

#@<OUT> classicresult.column_names
NAME
      column_names - Gets the columns on the current result.

SYNTAX
      <ClassicResult>.column_names

#@<OUT> classicresult.columns
NAME
      columns - Gets the column metadata for the columns on the active result.

SYNTAX
      <ClassicResult>.columns

#@<OUT> classicresult.execution_time
NAME
      execution_time - Retrieves a string value indicating the execution time
                       of the executed operation.

SYNTAX
      <ClassicResult>.execution_time

#@<OUT> classicresult.fetch_all
NAME
      fetch_all - Returns a list of Row objects which contains an element for
                  every record left on the result.

SYNTAX
      <ClassicResult>.fetch_all()

RETURNS
       A List of Row objects.

DESCRIPTION
      If this function is called right after executing a query, it will return
      a Row for every record on the resultset.

      If fetchOne is called before this function, when this function is called
      it will return a Row for each of the remaining records on the resultset.

#@<OUT> classicresult.fetch_one
NAME
      fetch_one - Retrieves the next Row on the ClassicResult.

SYNTAX
      <ClassicResult>.fetch_one()

RETURNS
       A Row object representing the next record in the result.

#@<OUT> classicresult.get_affected_row_count
NAME
      get_affected_row_count - The number of affected rows for the last
                               operation.

SYNTAX
      <ClassicResult>.get_affected_row_count()

RETURNS
       the number of affected rows.

DESCRIPTION
      This is the value of the C API mysql_affected_rows(), see
      https://dev.mysql.com/doc/refman/5.7/en/mysql-affected-rows.html

#@<OUT> classicresult.get_auto_increment_value
NAME
      get_auto_increment_value - Returns the last insert id auto generated
                                 (from an insert operation)

SYNTAX
      <ClassicResult>.get_auto_increment_value()

RETURNS
       the integer representing the last insert id

#@<OUT> classicresult.get_column_count
NAME
      get_column_count - Retrieves the number of columns on the current result.

SYNTAX
      <ClassicResult>.get_column_count()

RETURNS
       the number of columns on the current result.

#@<OUT> classicresult.get_column_names
NAME
      get_column_names - Gets the columns on the current result.

SYNTAX
      <ClassicResult>.get_column_names()

RETURNS
       A list with the names of the columns returned on the active result.

#@<OUT> classicresult.get_columns
NAME
      get_columns - Gets the column metadata for the columns on the active
                    result.

SYNTAX
      <ClassicResult>.get_columns()

RETURNS
       a list of column metadata objects containing information about the
      columns included on the active result.

#@<OUT> classicresult.get_execution_time
NAME
      get_execution_time - Retrieves a string value indicating the execution
                           time of the executed operation.

SYNTAX
      <ClassicResult>.get_execution_time()

#@<OUT> classicresult.get_info
NAME
      get_info - Retrieves a string providing information about the most
                 recently executed statement.

SYNTAX
      <ClassicResult>.get_info()

RETURNS
       a string with the execution information

#@<OUT> classicresult.get_warning_count
NAME
      get_warning_count - The number of warnings produced by the last statement
                          execution.

SYNTAX
      <ClassicResult>.get_warning_count()

RETURNS
       the number of warnings.

#@<OUT> classicresult.get_warnings
NAME
      get_warnings - Retrieves the warnings generated by the executed
                     operation.

SYNTAX
      <ClassicResult>.get_warnings()

RETURNS
       a list containing a warning object for each generated warning.

DESCRIPTION
      Each warning object contains a key/value pair describing the information
      related to a specific warning.

      This information includes: level, code and message.

#@<OUT> classicresult.has_data
NAME
      has_data - Returns true if the last statement execution has a result set.

SYNTAX
      <ClassicResult>.has_data()

#@<OUT> classicresult.help
NAME
      help - Provides help about this class and it's members

SYNTAX
      <ClassicResult>.help()

#@<OUT> classicresult.info
NAME
      info - Retrieves a string providing information about the most recently
             executed statement.

SYNTAX
      <ClassicResult>.info

#@<OUT> classicresult.next_data_set
NAME
      next_data_set - Prepares the SqlResult to start reading data from the
                      next Result (if many results were returned).

SYNTAX
      <ClassicResult>.next_data_set()

RETURNS
       A boolean value indicating whether there is another result or not.

#@<OUT> classicresult.warning_count
NAME
      warning_count - The number of warnings produced by the last statement
                      execution.

SYNTAX
      <ClassicResult>.warning_count

#@<OUT> classicresult.warnings
NAME
      warnings - Retrieves the warnings generated by the executed operation.

SYNTAX
      <ClassicResult>.warnings
