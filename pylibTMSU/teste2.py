



WAIT.until(ec.element_to_be_clickable((By.ID, 'EJRodapeManifesto_ibtnIncluir'))).click()
# Acha o Número do Manivesto e guarda na variavel
numero_manifesto = WAIT.until(ec.element_to_be_clickable((By.ID, 'lblNrManifesto')))
# Clica no label
numero_manifesto.click()
time.sleep(3)
# Numero do ma
texto = numero_manifesto.text
print(f'Num Manifesto ID: {str(texto)}')