/* Objective function */
min: 6 xa + 2 xb + 6 xc + 7 xd +
     4 ya + 9 yb + 5 yc + 3 yd +
     8 za + 8 zb + 1 zc + 5 zd;

/* Variable bounds */
supplyx: xa + xb + xc + xd <= 30;
supplyy: ya + yb + yc + yd <= 25;
supplyz: za + zb + zc + zd <= 21;

demanda: xa + ya + za >= 15;
demandb: xb + yb + zb >= 17;
demandc: xc + yc + zc >= 22;
demandd: xd + yd + zd >= 12;
