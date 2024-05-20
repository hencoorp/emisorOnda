import time  
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds 

def main():
    BoardShim.enable_dev_board_logger()  # Habilitar el registro de la placa de desarrollo
    params = BrainFlowInputParams()  # Crear un objeto para configurar los parámetros de entrada
    #params.serial_port = "COM3"  # Configurar el puerto serial COM3 para la conexión con la placa Cyton
    board = BoardShim(BoardIds.SYNTHETIC_BOARD.value, params)  # Crear un objeto de la placa Cyton con los parámetros configurados
    board.prepare_session()  # Preparar la sesión de la placa para la adquisición de datos
    board.start_stream()  # Iniciar la transmisión de datos desde la placa
    BoardShim.log_message(LogLevels.LEVEL_INFO.value, 'start sleeping in the main thread')  
    time.sleep(0.004)  # Suspender la ejecución durante 4 milisegundos
    data = board.get_board_data()  # Obtener los datos de la placa
    board.stop_stream()  # Detener la transmisión de datos
    board.release_session()  # Liberar los recursos de la sesión de la placa
    print(data)

if __name__ == "__main__":
    main()

