import schema

def dat_hnd(rec: any) -> any:
    print("*************************")
    print(rec)
    return [rec]

def schema_handler_v1(sch: schema.Schema) -> (schema.Schema, any):
    return sch, 
