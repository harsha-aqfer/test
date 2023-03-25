import schema
import time

def dat_hnd(rec: any) -> any:
    return [rec]

def schema_handler_v1(sch: schema.Schema) -> (schema.Schema, any):
    time.sleep(10)
    return sch, dat_hnd
