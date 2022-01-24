import aufgabe_ls3_01a as gr
import aufgabe_ls3_01b as tf
while 1:
    print ("(0) - Beenden \n(1) - Addieren \n(2) - Subtrahieren \n(3) - Multiplizieren \n(4) - Dividieren \n(5) - Potenz \n(6) - Wurzel \n(7) - Sinus \n(8) - Cosinus \n(9) - Tangens \n(10) - ASinus \n(11) - ACosinus \n(12) - ATangens")
    rart = input ("Wähle Rechenart aus: ")

    if (rart == "0"):
        break
    elif (rart == "1"):
        in1 = int(input("Gib erste Zahl: "))
        in2 = int(input("Gib zweite Zahl: "))
        ergebnis = gr.addieren(in1,in2)
        print(in1,"+",in2,"=",ergebnis)
    elif (rart == "2"):
        in1 = int(input("Gib erste Zahl: "))
        in2 = int(input("Gib zweite Zahl: "))
        ergebnis = gr.subtrahieren(in1,in2)
        print(in1,"-",in2,"=",ergebnis)
    elif (rart == "3"):
        in1 = int(input("Gib erste Zahl: "))
        in2 = int(input("Gib zweite Zahl: "))
        ergebnis = gr.multiplizieren(in1,in2)
        print(in1,"*",in2,"=",ergebnis)
    elif (rart == "4"):
        in1 = int(input("Gib erste Zahl: "))
        in2 = int(input("Gib zweite Zahl: "))
        ergebnis = gr.dividieren(in1,in2)
        print(in1,":",in2,"=",ergebnis)
    elif (rart == "5"):
        in1 = int(input("Gib erste Zahl: "))
        in2 = int(input("Gib die Potenz an: "))
        ergebnis = gr.potenz(in1,in2)
        print(in1,"hoch",in2,"=",ergebnis)
    elif (rart == "6"):
        in1 = int(input("Gib die Zahl für die Wurzel an: "))
        ergebnis = gr.wurzel(in1)
        print("Die Wurzel von",in1,"ist",ergebnis)
    elif (rart == "7"):
        in1 = int(input("Gib die Zahl für den Sinus an: "))
        ergebnis = tf.sinus(in1)
        print("Der Sinus von",in1,"ist",ergebnis)
    elif (rart == "8"):
        in1 = int(input("Gib die Zahl für den Cosinus an: "))
        ergebnis = tf.cosinus(in1)
        print("Der Cosinus von",in1,"ist",ergebnis)
    elif (rart == "9"):
        in1 = int(input("Gib die Zahl für den Tangens an: "))
        ergebnis = tf.tangens(in1)
        print("Der Tangens von",in1,"ist",ergebnis)
    elif (rart == "10"):
        in1 = int(input("Gib die Zahl für den ASinus an: "))
        ergebnis = tf.aSin(in1)
        print("Der ASinus von",in1,"ist",ergebnis)
    elif (rart == "11"):
        in1 = int(input("Gib die Zahl für den ASinus an: "))
        ergebnis = tf.aCos(in1)
        print("Der ACos von",in1,"ist",ergebnis)
    elif (rart == "12"):
        in1 = int(input("Gib die Zahl für den ATan an: "))
        ergebnis = tf.aTan(in1)
        print("Der ATan von",in1,"ist",ergebnis)
