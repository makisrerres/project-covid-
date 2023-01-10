# Project Covid-19
Εικονοποίηση της εξέλιξης του Covid
## Γενικά
Αυτή η εφαρμογή δημιουργήθηκε με αφορμή την ομαδική εργασία του μαθήματος Εισαγωγή στους Υπολογιστές, είναι γραμμένη σε Python και σκοπός της είναι η εικονοποίηση της εξέλιξης του Covid-19. Βασικές βιβλιοθήκες που χρησιμοποιύμε είναι: Tkinter, Customtkinter, RangeSlider, Matplotlib, Sqlite3, Pandas, Datetime και Os

## Οδηγίες χρήσης εφαρμογής
Όταν ανοίγει ο χρήστης το πρόγραμμα εμφανίζεται ένα περιβάλλον της customtkinter σε darkmode. Αριστερά υπάρχουν 4 επιλογές-switches, 1 για τα κρούσματα, 1 για
τους θανάτους, 1 για τους εμβολιασμούς, 1 για τα ημερήσια δεδομένα. Ο χρήστης από τις πρώτες 3 επιλογές μπορεί να επιλέξει περισσότερες από μία και να
εμφανιστούν στον πίνακα που βρίσκεται στη μέση της οθόνης, στο πάνω μέρος της ποία υπάρχουν 2 dropdown menus που μπορεί να επιλέξει τις χώρες. Έχουμε ορίσει
ως προεπιλεγμένη πρώτη χώρα την Ελλάδα, χωρίς να έχουμε δεύτερη χώρα. Στο κάτω μέρος της μεσαίας στήλης υπάρχει 1 slider, μέσω του οποίου ο χρήστης επιλέγει την
αρχική και την τελική ημερομηνία. Δεξιά εμφανίζονται οι μέγιστες τιμές κρουσμάτων,κλπ... για τη χώρα που επιλέξαμε. Όταν επιλέξει κάποιο άλλο switch ο
χρήστης πρέπει να πατήσει refresh για να ανανεωθούν τα δεδομένα του γραφήματος. Επιπλέον, υπάρχει ένα ακόμα switch στην πρώτη στήλη με τα ημερήσια δεδομένα.
Όταν πατηθεί εμφανίζει ακριβώς από κάτω 3 radiobuttons με τις ίδιες επιλογές των υπολοίπων switch ,απλώς αφορούν σε ημερήσια δεδομένα αυτά που εμφανίζονται
στο πρόγραμμα. Στη δεξιά στήλη υπάρχουν και δύο επιλογές για την εναλλαγή του φόντου σε φωτεινό ή σκοτεινό, αλλά και για μεγέθυνση ή σμίκρυνση του παραθύρου
σε μία κλίμακα από 80% μέχρι 120%. Οφείλουμε να τονίσουμε ότι λόγω του μεγάλου όγκου δεδομένων το πρόγραμμα καθυστερεί να λειτουργήσει, αλλά αυτό ο χρήστης
το αντιλαμβάνεται μέσω ενός loadscreen που έχουμε τοποθετήσει.
Εάν θεωρείτε ότι η γραφική παράσταση έχει κολλήσει, παρακαλώ πατήστε το "refresh button".

>Συνολικές τιμές
![Screenshot 2023-01-09 094153](https://user-images.githubusercontent.com/47256274/211260327-8f48a8cb-f932-48ce-aefd-dcecb9ea18f4.png)

>Ημερήσιες τιμές
![Screenshot 2023-01-07 125845](https://user-images.githubusercontent.com/47256274/211259992-1d8fc5a6-f6fc-4020-8ee8-f7ad803fc94d.png)

## Οδηγίες εγκατάστασης
Υπάρχουν δύο τρόποι εγκατάστασης της εφαρμογής: Α) executable και Β) αρχεία κώδικα Python

### A) executable (προς το παρόν μη διαθέσιμο μέσω github λόγω περιορισμών μεγέθους αρχείου)
1. Λήψη αρχείου customcovidV2.zip **(προσωρινή λύση: [customcovidV2.zip](https://drive.google.com/file/d/1BY2fnam-CRK8390DtQjyOmQPwtAwEBhR/view?usp=sharing))**
2. Εξαγωγή αρχείου
3. Άνοιγμα αρχείου customcovidV2.exe

### B) αρχεία κώδικα Python
1. Κατέβασμα βιβλιοθηκών customtkinter,matplotlib,RangeSlider, pandas.
2. Λήψη αρχείου customcovidV2_Python.zip
3. Εξαγωγή αρχείου
4. Άνοιγμα αρχείου customcovidV2.py
