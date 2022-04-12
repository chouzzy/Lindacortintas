from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Snipped
from numpy import random



def index(request):
   x = random.randint(0,3)
   numbers = ['5516996092936','5516997093759','5516996092935','5516991439381']
   print(x)
   return render(request, 'index.html', 
   {
      #Container 1 (INDEX)
      'Banner_Title_1':'Sensação de casa nova', 
      'Banner_Desc_1':'Tire os planos do papel e os coloque na parede', 

      'Banner_Title_2':'Tintas de excelente qualidade', 
      'Banner_Desc_2':'Aqui você encontra as melhores marcas e ótimos preços!', 
      
      'Banner_Title_3':'Sua casa como você imagina', 
      'Banner_Desc_3':'Mas se não pintar nenhuma ideia, nós ajudamos você :)', 

      'Promo_icon_1':'Parcelamento em até 5x',
      'Promo_icon_2':'Frete grátis para até 50km!',
      'Promo_icon_3':"100% seguro!",
      
      # CONTAINER 2
      'About_us_title_1':"Quem somos",

      'About_us_text_1':'A Lindacor Tintas foi fundada em 1996, em Ribeirão Preto, com a missão de atender com excelência e cuidado os clientes da região. O foco sempre foi o atendimento e qualidade dos produtos, o que proporcionou a inauguração da segunda loja na cidade, em 2009. A capacitação das equipes é prioridade e constante, tal qual a parceria com fornecedores, que desenvolvem linhas de produtos com as mais novas tecnologias',

      'About_us_title_2':"A Lindacor Tintas é associada ao grupo Coopertintas",

      'About_us_text_2':'A Coopertintas, foi fundada no dia 30 de maio de 2012, é a união de empresas de varejo do segmento de tintas de Ribeirão Preto e região. Possui como foco estratégico: unir para poder crescer, aumento de competitividade e excelência em qualidade. A Coopertintas tem sua linha própria de produtos.',

      #CONTAINER 3
      'Products_line_title':"Conheça já nossos produtos!",
      'Products_line_1':"Linha imobiliária",
      'Products_line_2':"Linha industrial",
      'Products_line_3':"Acessórios para pinturas",
      'Products_line_4':"Impermeabilizantes",
      'Products_line_5':"Solventes",

      #CONTAINER 4
      'Partners_title':"Principais parceiros",

      #CONTAINER 5
      'Contact_title':"Nossas lojas",

      'Contact_address_1':"LOJA 1: Rua João Guião 1056",
      'Contact_phone_1':"(16) 3637-2108",
      'Contact_whatsapp_first_1':"(16) 99609-2936",
      'Contact_whatsapp_second_1':"(16) 99709-3759",

      'Contact_address_2':"LOJA 2: Av. Caramuru 2055",
      'Contact_phone_2':"(16) 3621-2108",
      'Contact_whatsapp_first_2':"(16) 99609-2935",
      'Contact_whatsapp_second_2':"(16) 99143-9381",

      'Contact_email_awer':"contato@awer.co",
      'Contact_email_lindacor':"contato@lindacortintas.com.br",
      'Contact_created_by':"created by",
      'Contact_creator_name':"awer.co",
      'button_zap_number':numbers[x],

      'Contact_rights':"Lindacor Tintas ®  - Todos os direitos reservados",

   })
# def second_page(request):
#    return render(request, 'second_page.html')

def snippet_detail(request,slug):
   snippet = get_object_or_404(Snipped, slug=slug)
   return HttpResponse(f'Essa deveria ser o detalhe de visualização para o slug do {slug}')

def handler404(request, exception):
   return render(request,'not_found.html')