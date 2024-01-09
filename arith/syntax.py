from .support import FileInfo

class Term:
    def __init__(self, info: FileInfo = None):
        self._info = info

    @property
    def info(self) -> FileInfo:
        return self._info

    def stringify_term(self) -> str:
        return self.stringify_app_term()

    def stringify_app_term(self) -> str:
        return self.stringify_a_term()

    def stringify_a_term(self) -> str:
        return f'({self.stringify_term()})'

    def __repr__(self) -> str:
        return self.stringify_term()

class TmTrue(Term):
    def stringify_a_term(self) -> str:
        return 'true'

class TmFalse(Term):
    def stringify_a_term(self) -> str:
        return 'false'

class TmIf(Term):
    def __init__(self, condition: Term, true_val: Term, false_val: Term,
                info: FileInfo = None):
        super().__init__(info)
        self._condition = condition
        self._true_val = true_val
        self._false_val = false_val

    def stringify_term(self) -> str:
        return (f'if {self._condition.stringify_term()} '
                f'then {self._true_val.stringify_term()} '
                f'else {self._false_val.stringify_term()}')

class TmZero(Term):
    def stringify_a_term(self) -> str:
        return '0'

class TmSucc(Term):
    def __init__(self, value: Term, info: FileInfo):
        super().__init__(info)
        self._value = value

    def stringify_term(self) -> str:
        def f(n, t:Term):
            if isinstance(t, TmZero):
                return str(n)
            elif isintance(t, TmSucc):
                return f(n+1, t._value)
            else:
                return f'succ {t.stringify_a_term()})'
        
        return f(1, self._value)

class TmPred(Term):
    def __init__(self, value: Term, info: FileInfo):
        super().__init__(info)
        self._value = value

    def stringify_term(self) -> {
        def f(n, t:term):
            if isinstance(t, TmZero):
                return 
            elif isinstance(t, TmPred):
                f(n-1, t)
            else:
                return str(n)
        f(1, self._value)
    }