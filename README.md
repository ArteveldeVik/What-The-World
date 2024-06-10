# Realtime Object Detection and Art Generation

## Overzicht
Deze Python-code gebruikt de `YOLO` objectdetectiemodel om objecten in realtime te detecteren via een webcam feed. Daarnaast genereert het beschrijvingen van de gedetecteerde objecten en creëert kunstwerken op basis van deze beschrijvingen.

## Benodigde Modules
De code maakt gebruik van de volgende Python-bibliotheken en -modules:
- `cv2` (OpenCV): Voor het openen en verwerken van webcam feed.
- `ultralytics` (YOLO): Voor objectdetectie.
- `helpers` (aangepaste module): Bevat de functie `predict_and_detect`.
- `CommentatorAgent` (aangepaste module): Bevat de functie `generate_conversation`.
- `creativeAgent` (aangepaste module): Bevat de functie `generate_art`.

## Installatie
Zorg ervoor dat je de volgende bibliotheken geïnstalleerd hebt:
```sh
pip install opencv-python ultralytics
```

## Gebruik
1. **Laad het YOLO-model**:
    ```python
    model = YOLO('/Users/viksluijter/Desktop/Tech 2 - EXAMEN/datasets/runs/detect/train/weights/best.pt')
    ```

2. **Open de webcam**:
    ```python
    cap = cv2.VideoCapture(0)
    ```

3. **Lees en verwerk frames van de webcam**:
    ```python
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            result_img, webcam_objects = predict_and_detect(model, frame, classes=[], conf=0.5)
            cv2.imshow('Webcam', result_img)
            print(webcam_objects)
            process_frame(webcam_objects)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    ```

4. **Verwerk de gedetecteerde objecten**:
    ```python
    def process_frame(objects):
        scene_description = generate_conversation(objects)
        print(scene_description)
        if scene_description:
            generate_art(scene_description)
    ```

5. **Release de video capture en sluit vensters**:
    ```python
    cap.release()
    cv2.destroyAllWindows()
    ```

## Functies
- **predict_and_detect(model, frame, classes, conf)**:
    - Gebruikt het model om objecten in een frame te detecteren.
    - `model`: Het geladen YOLO-model.
    - `frame`: Een enkel beeldframe van de webcam.
    - `classes`: De klassen van objecten om te detecteren (leeg voor alle klassen).
    - `conf`: De vertrouwensdrempel voor detecties.

- **generate_conversation(objects)**:
    - Genereert een beschrijving van de gedetecteerde objecten.

- **generate_art(description)**:
    - Creëert kunstwerken op basis van de gegenereerde beschrijving.

## Afsluiting
Deze code toont een combinatie van objectdetectie, conversatiegeneratie en creatieve kunstgeneratie in realtime via een webcam. Druk op de 'q'-toets om het programma te beëindigen.

