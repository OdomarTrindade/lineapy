import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.STATIC,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="foo()",
    session_name=None,
    user_name=None,
    hardware_spec=None,
    libraries=[],
)
call_1 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=1,
    col_offset=0,
    end_lineno=1,
    end_col_offset=5,
    arguments=[],
    function_name="foo",
    function_module=None,
    locally_defined_function_id=None,
    assigned_variable_name=None,
    value=None,
)