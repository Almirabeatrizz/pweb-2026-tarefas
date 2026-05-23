from django.shortcuts import render

def index(request):
    return render(request, "index.html")
    
def usuarios(request):
    lista_usuarios = [
        {
            'nome' : 'Gabriely Marcelino',
            'matricula' : '2024114',
            'idade' : '18', 
            'cidade' : 'Bom Jesus',
        },
        {
            'nome' : 'Emanuelly Maria',
            'matricula' : '2023118',
            'idade' : '18', 
            'cidade' : 'Bom Jesus',
        }, 
        {
            'nome' : 'Joao victor',
            'matricula' : '2023113',
            'idade' : '19', 
            'cidade' : 'Natal',
        },
        {
            'nome' : 'Sandrielly Oliveira ',
            'matricula' : '2023117',
            'idade' : '19', 
            'cidade' : 'Natal',
        },
            {
            'nome' : 'Joyce Kelly ',
            'matricula' : '2025114',
            'idade' : '16', 
            'cidade' : 'Parnamirim',
        }
    ]

    return render(request,'usuarios.html', {'usuarios': lista_usuarios})
