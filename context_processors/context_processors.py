from ui.models import UIFooter

def footer(request):
	return { 'footer_data': UIFooter.objects.get() }
	