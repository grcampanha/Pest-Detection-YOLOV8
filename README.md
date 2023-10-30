<div style="display: inline_block" ><br>
  <h1 align="center">
   <img align="center" alt="" height="50" width="60" src="https://avatars.githubusercontent.com/u/26833451?s=200&v=4"> Detecção de Pragas utilizando YOLOV8 <img align="center" alt=" height="50" width="60" src="https://avatars.githubusercontent.com/u/26833451?s=200&v=4">
  

### ⚠️Aviso⚠️
- Para utilização do multithread em duas telas é necessário conectar duas câmeras no PC

### 📋Sobre📋
- Código para detecção de Pragas em plantações, complementando um projeto de robô autônomo

- O código se consiste em um sistema de detecção de pragas.
<h1 align="center">
  <img alt="NextLevelWeek" title="#NextLevelWeek" src="https://github.com/grcampanha/Pest-Detection-YOLOV8/blob/main/PlantVision%20YOLOV8/imgs/lettuce-pest1.png" />
</h1>

- Foi criado um robô autônomo para o mapeamento de pragas numa plantação.

<h1 align="center">
  <img alt="NextLevelWeek" title="#NextLevelWeek" width="55%" src="https://github.com/grcampanha/Pest-Detection-YOLOV8/blob/main/PlantVision%20YOLOV8/imgs/robo/robo.jpg" />
</h1>


### 💻YoloV8 💻

- Para utilização do algoritmo YOLO v8, desenvolvemos um script básico que utiliza duas webcam's para detecção de pragas.

<h4 align="center">Importando as bibliotecas necessárias</h4>

```bash
import threading
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
```

<h4 align="center">Criando uma Função e Definindo o Modelo de Detecção</h4>

```bash
def CV(cam):  #Definindo a função CV()
    model = YOLO(r"...\PlantVision YOLOV8\runs\detect\train\weights\best.pt")  #Importando o Modelo de Detecção
    model.predict(source=f"{cam}", show=True, imgsz=512, conf=0.2, max_det=5, verbose=False)  #Salvando os Predicts para o reconhecimento e definindo a entrada de Cam para uma var
    # "source" é a câmera de entrada | "show" é a var para mostrar ou não a tela | "imgsz" é o tamanho da imagem | "conf" é a confiança da detecção | "max_det" é o máximo de detecção numa tela | "verbose" é os prints em terminal
```

<h4 align="center">Definindo a Função de Threads</h4>

```bash
def main(): #Definimos a função main()
    thread1 = threading.Thread(target=CV, args=(1,))  #Adicionamos a função da primeira thread onde "1" é a câmera considerada
    thread2 = threading.Thread(target=CV, args=(2,))  #Adicionamos a função da segunda thread onde "2" é a câmera considerada
    
    thread1.start()  #Iniciamos a Thread1
    thread2.start()  #Iniciamos a Thread2

    thread1.join()  #Bloqueia a execução do programa principal até que a thread1 termine
    thread2.join()  #Bloqueia a execução do programa principal até que a thread2 termine
```

<h4 align="center">Iniciando o Multithreading</h4>

```bash
if __name__ == "__main__":  #Verifica se o programa está sendo executado
    main()  #Inicia a função main() 
```
