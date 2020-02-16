class EvaluationException(Exception):
    pass


def toNumber(number):
    if "." in number:
        return float(number)
    else:
        return int(number)


def getIdentifier(name):
    if name in globalEnv:
        return globalEnv[name]


class Functions:
    def plus(params):
        result = 0
        for x in params:
            result += x
        return result


func = Functions


globalEnv = {
    '+': func.plus
}


def execute(syntaxtree):
    result = []
    for x in syntaxtree:
        if isinstance(x, tuple):
            if x[0] == "number":
                result.append(toNumber(x[1]))
            elif x[0] == "string":
                result.append(x[1])
            elif x[0] == "identifier":
                result.append(getIdentifier(x[1]))
        elif isinstance(x, list):
            if x[0][0] != "identifier":
                raise EvaluationException("Identifiers must be used for procedures.")
            function = getIdentifier(x[0][1])
            params = execute(x[1:])
            result.append(function(params))
    return result
