LETTER	[a-zA-Z]
NON_ZERO_DIGIT	[1-9]
DIGIT	0|{NON_ZERO_DIGIT}
IDENTIFIER	{LETTER}({LETTER}|{DIGIT})*
NUMBER	0|("-"{1}){NON_ZERO_DIGIT}{DIGIT}*
NATURAL_NUMBER	0|{NON_ZERO_DIGIT}{DIGIT}*
TEXT	"\""{CHAR}"\""
CHAR	[{LETTER}{DIGIT} ]
SEPARATOR [()"{""}""." ,"[""]"] scris toate separat
%%
"+"	{printf("%s\n","PLUS");}
"-"	{printf("%s\n","MINUS");}
"="	{printf("%s\n","ASSIGN");}
"*"	{printf("%s\n","MULTIPLY");}
"/"	{printf("%s\n","DIVIDE");}
"<"	{printf("%s\n","SMALLER");}
"<="	{printf("%s\n","SMALLER EQUAL");}
">"	{printf("%s\n","GREATER");}
">="	{printf("%s\n","GREATER EQUAL");}
"=="	{printf("%s\n","EQUALS");}
"=/="	{printf("%s\n","DIFFERENT");}
"start"	{printf("%s\n","START");}
"define"	{printf("%s\n","DEFINE");}
"as"	{printf("%s\n","AS");}
"text"	{printf("%s\n","TEXT");}
"read"	{printf("%s\n","READ");}
"show"	{printf("%s\n","SHOW");}
"condition"	{printf("%s\n","CONDITION");}
"otherwise"	{printf("%s\n","OTHERWISE");}
"end"	{printf("%s\n","END");}
"number"	{printf("%s\n","NUMBER");}
"while"	{printf("%s\n","WHILE");}
"repeat"	{printf("%s\n","REPEAT");}
"array"	{printf("%s\n","ARRAY");}
"of"	{printf("%s\n","OF");}
{IDENTIFIER} { printf( "IDENTIFIER: %s\n", yytext );}
{NUMBER} { printf( "NUMBER: %s\n", yytext );}
{NATURAL_NUMBER} { printf( "NATURAL_NUMBER: %s\n", yytext );}
{TEXT} { printf( "TEXT: %s\n", yytext );}
%%

main( argc, argv )
int argc;
char **argv;
    {
        ++argv, --argc;	/* skip over program name */
        if ( argc > 0 )
            yyin = fopen( argv[0], "r" );
        else
            yyin = stdin;
    yylex();
    }

#ifndef yywrap
   yywrap() { return 1; }
#endif
