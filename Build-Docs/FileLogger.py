import logging

class FileLogger:


  loggerFiles = {
      "Data-Preparation": "Build-Docs\DataPreparation.log"
    }
  def __init__(self, phase):
   
    self.phase = phase
    self.FileLoc=self.loggerFiles[phase]
    # Configure logging levelss
    self.levels = {
      "debug": logging.DEBUG,
      "info": logging.INFO,
      "error": logging.ERROR,
      "warning":logging.WARNING,
      "critical":logging.CRITICAL
    }
    self.logger = logging.getLogger(phase)


  def log(self, level, message):
    self.logger.setLevel(logging.DEBUG) 
    logging.basicConfig(filename=self.FileLoc, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to a file')


# Example
logger = FileLogger("training")
logger.log("debug", "Starting training process...")
logger.log("info", "Training on epoch 1")
logger.log("error", "Encountered an error during training")

