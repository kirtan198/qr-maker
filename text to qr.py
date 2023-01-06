import qrcode as qr
inp=input('enter text')
img=qr.make(inp)
img.save("krisnaa.png")