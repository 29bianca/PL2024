# Gramática
## Símbolos Terminais

```sql
T = {'?', '!', '=', '+', '-', '*', '/', '(', ')', var, num}

## Símbolos Não Terminais
```sql
N = {S, exp1, op1, exp2, op2, exp3}

## Símbolo Inicial
```sql
S = S

## Regras de Produção

P = {
    S -> '?' var           LA = {'?'}
       | var '=' exp1      LA = {var}
       | '!' exp1          LA = {'!'}

    exp1 -> exp2 op1       LA = {'(', var, num}

    op1 -> '+' exp1        LA = {'+'}
         | '-' exp1        LA = {'-'}
         | ε               LA = {')', $}

    exp2 -> exp3 op2       LA = {'(', var, num}

    op2 -> '*' exp1        LA = {'*'}
         | '/' exp1        LA = {'/'}
         | ε               LA = {')', $}

    exp3 -> '(' exp1 ')'   LA = {'('}
          | var            LA = {var}
          | num            LA = {num}
}