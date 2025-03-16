import asyncio
from render.camera.utils import *
from world.generation import checkChunk

async def cameraMove(data):
    cameraPivot.position += mouse.relative.x * rotations[rotationNumber][1][0] * 0.25 * (cameraPivot.y + 51)
    cameraPivot.position += mouse.relative.y * rotations[rotationNumber][1][1] * 0.25 * (cameraPivot.y + 51)
    verifyWorldLimit()
    checkChunk(data)


async def setCameraToCenter(data):
    cameraPivot.position = cameraPivot.position * Vec3(0, 1, 0) + Vec3(-11.5, 0, 8.5) - getCameraPosition().y * rotations[rotationNumber][0] * Vec3(1, 0, 1)
    checkChunk(data)


async def cameraZoomIn(data):
    if cameraPivot.position * Vec3(0, 1, 0) > Vec3(0, -40, 0):
        cameraPivot.position += rotations[rotationNumber][0]
    verifyWorldLimit()
    checkChunk(data)


async def cameraZoomOut(data):
    if cameraPivot.position * Vec3(0, 1, 0) < Vec3(0, -5, 0):
        cameraPivot.position -= rotations[rotationNumber][0]
    verifyWorldLimit()
    checkChunk(data)


async def cameraRotateRight(data):
    global rotationNumber, goalRotation
    rotationNumber += 1
    if rotationNumber > 3:
        rotationNumber = 0
    goalRotation += Vec3(0, 90, 0)
    checkChunk(data)


async def cameraRotateLeft(data):
    global rotationNumber, goalRotation
    rotationNumber -= 1
    if rotationNumber < 0:
        rotationNumber = 3
    goalRotation -= Vec3(0, 90, 0)
    checkChunk(data)


async def cameraRotateUpdate():
    global goalRotation
    if camera.rotation != goalRotation:
        if goalRotation < camera.rotation:
            camera.rotation -= Vec3(0, 5, 0)
        else:
            camera.rotation += Vec3(0, 5, 0)



def verifyWorldLimit():
    if (getCameraPosition() * Vec3(1, 0, 0)).x > worldLimit:
        cameraPivot.position = cameraPivot.position * Vec3(0, 1, 1) + Vec3(worldLimit - 11.5, 0, 0)
    elif (getCameraPosition() * Vec3(1, 0, 0)).x < -worldLimit:
        cameraPivot.position = cameraPivot.position * Vec3(0, 1, 1) + Vec3(-worldLimit - 11.5, 0, 0)
    if (getCameraPosition() * Vec3(0, 0, 1)).z > worldLimit:
        cameraPivot.position = cameraPivot.position * Vec3(1, 1, 0) + Vec3(0, 0, worldLimit + 8.5)
    elif (getCameraPosition() * Vec3(0, 0, 1)).z < -worldLimit:
        cameraPivot.position = cameraPivot.position * Vec3(1, 1, 0) + Vec3(0, 0, -worldLimit + 8.5)
