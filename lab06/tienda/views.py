from django.shortcuts import get_object_or_404,  render

from .models import Categoria, Producto

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]

    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    categoria_id = request.GET.get('categoria')

    if categoria_id:
        categoria = Categoria.objects.get(id=categoria_id)
        productos = productos.filter(categoria=categoria)

    context = {
        'categorias': categorias,
        'productos': productos,
        'product_list': product_list, 
        'titulo': "Ecomerce Ramirez"
        }
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto,pk=producto_id)
    
    print(producto.img_producto.url)  # Imprime la ruta de la imagen en la consola de tu servidor
    return render(request, 'producto.html', {'producto': producto, 'titulo': "Ecomerce Ramirez"})
