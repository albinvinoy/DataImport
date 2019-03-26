class schemaValidate:
    """
    A simple class to validate schema
    """
    def __init__(self):
        self.acceptParam = set(["INT", "INTEGER", "SMALLINT", "FLOAT", "CHAR", "VARCHAR"])
        self.noParam = set(["BOOL","BOOLEAN", "DATE", "TIME", "DATETIME", "TIMESTAMP", "YEAR"])
    
    def validate(self, validateArr):
        """ 
            param : validateArr
            return:  valided string
            ex. author_name,10,CHAR -> author_name CHAR(10)
            is_alive,1,BOOLEAN -> is_alive BOOLEAN
        """
        if validateArr[2].upper() in self.acceptParam:
            dType = "{}({})".format(validateArr[2].upper(), validateArr[1])
            return "{} {}".format( validateArr[0].upper(), dType )
        else:
            return "{} {}".format( validateArr[0].upper(), validateArr[2].upper() )

