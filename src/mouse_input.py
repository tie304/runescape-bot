import os
import time
import json
from pynput import mouse


class MouseInput:
    def __init__(self, objective, n_recordings):
        self.objective = objective
        self.n_recordings = n_recordings
        self.total_recordings = 0  # keeps track of each recording
        self.data_store = []

        with mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.join()

    def __str__(self):
        return "<MouseInput>"

    def on_click(self, x, y, button, pressed):

        if pressed:
            self.data_store.append({
                "x": x,
                "y": y,
                "button": str(button),
                "time": time.time()
            })

            self.total_recordings +=1

            if self.n_recordings:
                if self.total_recordings >= self.n_recordings:
                    self.save()
                    return False

    def on_scroll(self, *args):
        self.save()
        return False

    def save(self):
        data = json.dumps(self.data_store)
        path = os.path.join(os.getenv('DATA_DIR'), os.getenv('OBJECTIVE_DIR'), self.objective + ".json")
        if not os.path.exists(os.path.join(os.getenv('DATA_DIR'), os.getenv('OBJECTIVE_DIR'))):
            os.makedirs(os.path.join(os.getenv('DATA_DIR'), os.getenv('OBJECTIVE_DIR')))
        with open(path, "w+") as file:
            file.write(data)



