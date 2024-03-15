# --------------------------------------------------------------------------------
#1. Declarati un dictionar.

producatori = {"Asus":"Taiwan",
              "Dell":"SUA",
              "Huawei":"China",
              "Samsung":"Coreea de sud"}
print(producatori)

# --------------------------------------------------------------------------------
#2. Declarati un dictionar gol.

dictionar_gol = {}
print(dictionar_gol)

# --------------------------------------------------------------------------------
#3. Adaugati un element nou in dictionar folosind functia update() si respectiv
#   pe baza de cheie.

producatori.update({"Lenovo":"China"})    # aici, folosind functia UPDATE
producatori["Acer"] = "Taiwan"            # aici, pe baza de cheie-valoare
print(producatori)



# --------------------------------------------------------------------------------
#4. Extrageti un element din dictionar folosind metoda get() si respectiv
#   pe baza de cheie.

tara_producator_ales = producatori.get("Asus")
print(f"Laptopurile ASUS sunt produse in {tara_producator_ales}.")
print(f"Laptopurile Acer sunt produse in {producatori['Acer']}.")

# --------------------------------------------------------------------------------
#5. Stergeti un element din dictionar folosind functia pop() si respectiv
#   functia popitem(). Observati rezultatele.

producatori.pop("Lenovo")     # stergere folosind functia POP
print(f"Lista de producatori de laptopuri dupa ce am sters 'Lenovo' de pe lista:")
print(f"{producatori}")
producatori.popitem()         # sterge ultimul element din lista(dictionar)
print(f"Lista actualizata: {producatori}")



# --------------------------------------------------------------------------------
#6. Extrageti pe rand toate cheile, apoi toate valorile, si apoi toate item-urile
#   din dictionar.

print(f'Asa se extrag toate elementele, unul cate unul: {producatori.items()}')
print(f'Asa se extrag toate cheile din dictionar: {producatori.keys()}')
print(f'Asa se extrag toate valorile cheilor din dictionar: {producatori.values()}')



# --------------------------------------------------------------------------------
#7. Stergeti toate valorile din dictionar folosind metoda clear().

producatori.clear()

