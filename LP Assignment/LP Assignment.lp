/* Objective function */
max: 20 Dogberts + 16 Catberts + 15 Ratberts;

/* Variable bounds - constraints */

/* Weight (max: 2000 lbs)*/
Weight: 7 Dogberts + 8 Catberts + 6 Ratberts <= 2000;

/* Volume (max: 3200 cubic ft)*/
Volume: 15 Dogberts + 11 Catberts + 8 Ratberts <= 3200;

/* Packing Time (max: 1600 secs.)*/
PackingTime: 4 Dogberts + 5 Catberts + 7 Ratberts <= 1600;

/* Min/Max Order */
MinimumDogberts: 90 <= Dogberts;
MinimumCatberts: 50 <= Catberts;
MaximumRatberts: 140 >= Ratberts;

/* Force Integers */
/* int Dogberts, Catberts, Ratberts;  */