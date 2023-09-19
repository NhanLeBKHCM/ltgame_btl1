class GameSceneManager:
    def __init__(self, currentScene, scenes):
        self.currentScene = currentScene
        self.scenes = scenes

    def init_allScene(self):
        for scene in list(self.scenes.values()):
            scene.init()

    def getCurrentScene(self):
        return {"name": self.currentScene, "scene": self.scenes[self.currentScene]}

    def setCurrentScene(self, scene, state=None, data=None):
        if self.scenes:
            self.scenes[self.currentScene].end()
        self.currentScene = scene
        self.scenes[self.currentScene].start(state, data)

    def updateCurrentScene(self):
        self.scenes[self.currentScene].update()
