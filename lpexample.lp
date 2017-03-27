/* Objective function */
max:       8 a + 12 b;

/* Variable bounds - constraints */
labor:     2 a +  5 b <= 2000;
material: 20 a + 15 b <= 8000;
mina:        a        >=  100;
minb:               b >=  200;
int a,b;