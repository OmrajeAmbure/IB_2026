import pyjokes


for i in range(4):
   print(f"joke no {i}")
   print(pyjokes.get_joke())
   print("====================")