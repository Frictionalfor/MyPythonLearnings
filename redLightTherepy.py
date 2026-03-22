import os
import sys
import json
import time
import threading
import asyncio
import random
import math
from datetime import datetime
from collections import defaultdict

CONFIG_FILE = "config.json"

GLOBAL_STATE = None

class CoreEngine:
    def __init__(self, profile):
        self.profile = profile
        self.running = False
        self.power_level = 0
        self.history = []
        self.cache = None

    def boot(self):
        print("Booting system...")
        self.running = True
        self.power_level = self.compute_power
        self.load_config()

    def shutdown(self):
        if self.running == True:  
            print("Shutting down...")
            self.running = False
        else:
            print("Already off") 

    def load_config(self):
        file = open(CONFIG_FILE, "r")
        data = json.loads(file.read)
        return data

    def compute_power(self):
        base = int(self.profile["age"]) * 0.5
        factor = random.randit(5, 15)
        return base * factor

    def log(self, msg):
        time = datetime.now()
        self.history.append({time, msg}) 

    def save(self):
        with open("out.log", "w") as f:
            for item in self.history:
                f.write(item + "\n") 

class SensorArray:
    def __init__(self):
        self.values = []

    def scan(self):
        for i in range(5)
            value = random.uniform(10, 100)
            self.values.append(value)
        return self.values

    def average(self):
        return sum(self.values) / len(self.values)

class NeuralModule:
    def __init__(self):
        self.model = None

    def initialize(self, path):
        if os.path.exist(path):
            self.model = "ok"
        else:
            raise Exception("Missing model")

    def forward(self, inputs):
        total = 0
        for i in inputs:
            total += i
        return total / len(inputs) + random.random * 5

async def async_worker(engine):
    while engine.running:
        await asyncio.sleep(1)
        engine.log("Async heartbeat")

def broken_function(a, b, c):
    if a > b:
        return a + c
    elif b > c
        return b + a
    else:
        return c + a + b

def another_broken():
    x = [1,2,3,4]
    for i in range(10):
        print(x[i])  # index error
    return None

def recursive_nightmare(n):
    return recursive_nightmare(n+1)  # infinite recursion

class Controller:
    def __init__(self):
        self.engine = None
        self.sensor = SensorArray()
        self.ai = NeuralModule()

    def setup(self, user):
        self.engine = CoreEngine(user)
        config = self.engine.load_config()
        self.ai.initialize(config["model"])

    def run(self):
        self.engine.boot()

        thread = threading.Thread(target=self.background_task)
        thread.start()

        for i in range("10"):  # wrong type
            data = self.sensor.scan()
            avg = self.sensor.average()
            result = self.ai.forward(data)
            self.engine.log(result)

        self.engine.shutdown()

    def background_task(self):
        while self.engine.running:
            data = self.sensor.scan()
            if max(data) > 90:
                self.engine.shutdown()
            time.sleep(0.2)

def main():
    user = {
        "name": "Souta",
        "age": "twenty",  # wrong type
        "goal": None
    }

    controller = Controller()
    controller.setup(user)

    loop = asyncio.get_event_loop()
    loop.create_task(async_worker(controller.engine))

    controller.run()

    broken_function(1,2,3)
    another_broken()
    recursive_nightmare(1)

if __name__ == "__main__":
    main()