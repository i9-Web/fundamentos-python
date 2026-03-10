#Exemplos 8: Diferença simétrica (symmetric difference)
tecnologias_frontend = {"HTML", "CSS", "JavaScript", "React"}

tecnologias_backend = {"Python", "Node.js", "JavaScript", "MongoDB"}

# Diferença simétrica usando ^ ou symmetric_difference()
tecnologias_exclusivas = tecnologias_frontend ^ tecnologias_backend
tecnologias_exclusivas2 = tecnologias_frontend.symmetric_difference(
                                                tecnologias_backend)

print(f"Frontend: {tecnologias_frontend}")
print(f"Backend: {tecnologias_backend}")
print(f"Tecnologias exclusivas: {tecnologias_exclusivas}")
print(f"Tecnologias exclusivas: {tecnologias_exclusivas2}")

