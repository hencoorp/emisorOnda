""" 

import asyncio
import time
import json
import websockets
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

async def send_data():
    while True:
        try:
            BoardShim.enable_dev_board_logger()
            params = BrainFlowInputParams()
            board = BoardShim(BoardIds.SYNTHETIC_BOARD.value, params)
            board.prepare_session()
            board.start_stream()

            # Loop para intentar la conexión hasta que se establezca
            while True:
                try:
                    async with websockets.connect('wss://f27dfk-8765.csb.app') as websocket:
                        print("Conexión establecida con éxito.")
                        break  # Salir del bucle si la conexión es exitosa
                except Exception as e:
                    print(f"No se pudo conectar al servidor. Intentando de nuevo en 1 segundo...")
                    await asyncio.sleep(1)  # Esperar 1 segundo antes de intentar de nuevo

            # Bucle principal para enviar datos
            while True:
                start_time = time.time()
                data = board.get_current_board_data(250)
                print("Datos enviados:", data.tolist())  # Imprime los datos enviados

                await websocket.send(json.dumps(data.tolist()))

                elapsed_time = time.time() - start_time
                await asyncio.sleep(max(0, 1/250 - elapsed_time))

            board.stop_stream()
            board.release_session()
        except websockets.ConnectionClosed as e:
            print(f"Conexión cerrada: {e}")
        except Exception as e:
            print(f"Error: {e}")

async def main():
    await send_data()

if __name__ == "__main__":
    asyncio.run(main())
 """

""" import asyncio
import time
import json
import websockets
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

async def send_data():
    while True:
        try:
            BoardShim.enable_dev_board_logger()
            params = BrainFlowInputParams()
            board = BoardShim(BoardIds.SYNTHETIC_BOARD.value, params)
            board.prepare_session()
            board.start_stream()

            # Loop para intentar la conexión hasta que se establezca
            while True:
                try:
                    async with websockets.connect('wss://f27dfk-8765.csb.app') as websocket:
                        print("Conexión establecida con éxito.")
                        break  # Salir del bucle si la conexión es exitosa
                except Exception as e:
                    print(f"No se pudo conectar al servidor. Intentando de nuevo en 1 segundo...")
                    print(f"Error: {e}")  # Imprimir el error específico
                    await asyncio.sleep(1)  # Esperar 1 segundo antes de intentar de nuevo

            # Bucle principal para enviar datos
            while True:
                start_time = time.time()
                data = board.get_current_board_data(250)
                print("Datos enviados:", data.tolist())  # Imprime los datos enviados

                await websocket.send(json.dumps(data.tolist()))

                elapsed_time = time.time() - start_time
                await asyncio.sleep(max(0, 1/250 - elapsed_time))

                # Liberar recursos del tablero
                board.stop_stream()
                board.release_session()
        except websockets.ConnectionClosed as e:
            print(f"Conexión cerrada: {e}")
        except Exception as e:
            print(f"Error: {e}")

async def main():
    await send_data()

if __name__ == "__main__":
    asyncio.run(main())
 """


import asyncio
import time
import json
import websockets
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

async def send_data():
    try:
        BoardShim.enable_dev_board_logger()
        params = BrainFlowInputParams()
        board = BoardShim(BoardIds.SYNTHETIC_BOARD.value, params)
        board.prepare_session()
        board.start_stream()

        async with websockets.connect('wss://f27dfk-8765.csb.app') as websocket:
            print("Conexión establecida con éxito.")
            # Bucle principal para enviar datos
            while True:
                start_time = time.time()
                data = board.get_current_board_data(250)
                print("Datos enviados:", data.tolist())  # Imprime los datos enviados

                await websocket.send(json.dumps(data.tolist()))

                elapsed_time = time.time() - start_time
                await asyncio.sleep(max(0, 1/250 - elapsed_time))

        board.stop_stream()
        board.release_session()
    except websockets.ConnectionClosed as e:
        print(f"Conexión cerrada: {e}")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    await send_data()

if __name__ == "__main__":
    asyncio.run(main())
