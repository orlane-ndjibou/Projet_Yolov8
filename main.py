from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

TARGET_CLASS = "knife"  # change selon l'objet que tu veux surveiller

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    boxes = results[0].boxes  # liste des détections

    person_count = 0
    alert_triggered = False

    for box in boxes:
        class_id = int(box.cls[0])          # TODO: récupère l'ID de classe
        class_name = model.names[class_id]   # TODO: convertis en nom lisible

        print(f"Détection: {class_name} (ID: {class_id})")

        # TODO: si class_name == "person", incrémente person_count
        if class_name == "person":
            person_count += 1
        
        # TODO: si class_name == TARGET_CLASS, passe alert_triggered à True
        if class_name == TARGET_CLASS:
            alert_triggered = True


    annotated = results[0].plot()  # dessine les boîtes YOLO par défaut

    # TODO: utilise cv2.putText(annotated, texte, position, police, taille, couleur, épaisseur)
    # pour afficher "Personnes: X" en haut à gauche de l'image
    cv2.putText(annotated, f"Personnes: {person_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    # TODO: si alert_triggered, affiche un texte rouge "ALERTE" (grosse taille, couleur (0,0,255))
    if alert_triggered:
        cv2.putText(annotated, "ALERTE", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow("YOLO", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()