from django.contrib.auth.decorators import login_required  # Импортируем декоратор для проверки аутентификации пользователя
from django.views.generic import DetailView, CreateView  # Импортируем классы для обработки деталей объектов и создания объектов
from django.contrib.auth.mixins import LoginRequiredMixin  # Импортируем миксин для проверки аутентификации пользователя
from django.core.paginator import Paginator  # Импортируем класс для разбиения на страницы
from django.http import JsonResponse  # Импортируем JsonResponse для AJAX-ответа в формате JSON
from django.shortcuts import render  # Импортируем функцию для отображения шаблонов
from .models import Post, Message, CATEGORIES  # Импортируем модели Post и Message и список категорий CATEGORIES
from .forms import MessageForm, PostForm  # Импортируем формы для создания сообщений и постов

@login_required  # Применяем декоратор login_required, чтобы представление доступно только аутентифицированным пользователям
def user_messages(request):
    messages = Message.objects.filter(receiver=request.user)  # Получаем все сообщения, где текущий пользователь является получателем
    return render(request, 'user_messages.html', {'messages': messages})  # Отображаем шаблон 'user_messages.html' с переданным контекстом

def post_list(request):
    posts = Post.objects.all()  # Получаем все объекты модели Post
    paginator = Paginator(posts, 2)  # Создаем пагинатор, показывать по 2 поста на странице

    page_number = request.GET.get('page')  # Получаем номер запрошенной страницы из параметров GET запроса
    page_obj = paginator.get_page(page_number)  # Получаем объект текущей страницы с помощью пагинатора

    if request.is_ajax():  # Проверяем, является ли запрос AJAX-запросом
        data = {
            'html': render(request, 'post_list.html', {'page_obj': page_obj}).content.decode(),  # Отображаем шаблон 'post_list.html' с контекстом текущей страницы
            'has_next': page_obj.has_next()  # Передаем информацию о наличии следующей страницы
        }
        return JsonResponse(data)  # Возвращаем JSON-ответ с данными для AJAX-запроса

    return render(request, 'post_list.html', {'page_obj': page_obj})  # Отображаем шаблон 'post_list.html' с переданным контекстом

class PostDetailView(DetailView):
    model = Post  # Указываем модель Post, для которой будем показывать детали
    template_name = 'post_detail.html'  # Указываем имя шаблона, который будет использоваться для отображения деталей объекта
    context_object_name = 'post'  # Задаем имя переменной контекста, через которую получим объект поста

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  # Указываем модель Post, для которой будем создавать объекты
    form_class = PostForm  # Указываем форму, которая будет использоваться для создания объектов
    template_name = 'post_form.html'  # Указываем имя шаблона, который будет использоваться для отображения формы создания

    def form_valid(self, form):
        form.instance.author = self.request.user  # Устанавливаем автора поста как текущего пользователя
        return super().form_valid(form)  # Вызываем метод form_valid() родительского класса для сохранения объекта

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Получаем базовый контекст
        context['categories'] = CATEGORIES  # Добавляем список категорий в контекст
        return context  # Возвращаем контекст

class MessageCreateView(CreateView):
    model = Message  # Указываем модель Message, для которой будем создавать объекты
    form_class = MessageForm  # Указываем форму, которая будет использоваться для создания объектов
    template_name = 'message_form.html'  # Указываем имя шаблона, который будет использоваться для отображения формы создания

    def get_success_url(self):
        return self.get_object().post.get_absolute_url()  # Возвращаем URL, на который будет перенаправлен пользователь после успешного создания сообщения

    def form_valid(self, form):
        form.instance.sender = self.request.user  # Устанавливаем отправителя сообщения как текущего пользователя
        form.instance.receiver = self.get_object().author  # Устанавливаем получателя сообщения как автора объекта, к которому относится сообщение
        form.instance.post = self.get_object()  # Устанавливаем объект поста для сообщения
        return super().form_valid(form)  # Вызываем метод form_valid() родительского класса для сохранения объекта