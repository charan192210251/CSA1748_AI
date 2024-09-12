disease(diabetes, 'Low-sugar diet, high-fiber foods, lean proteins').
disease(hypertension, 'Low-sodium diet, rich in fruits and vegetables').
disease(heart_disease, 'Low-fat diet, omega-3 fatty acids, whole grains').
disease(obesity, 'Low-calorie diet, balanced macronutrients, regular meals').
disease(celiac_disease, 'Gluten-free diet, whole foods').
disease(kidney_disease, 'Low-protein diet, low-sodium, low-potassium').
disease(anemia, 'Iron-rich diet, vitamin C, leafy greens').
disease(gout, 'Low-purine diet, avoid red meat, alcohol reduction').

suggest_diet(Disease, Diet) :-
    disease(Disease, Diet),
    write('For '),
    write(Disease),
    write(', the recommended diet is: '),
    write(Diet),
    nl.
