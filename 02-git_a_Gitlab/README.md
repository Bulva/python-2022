## Práce s gitem a GitLabem
* [GitLab - prezentace](https://slides.com/bulva/gitlab)

### Založení repozitáře na GitLabu
1. Registrace a přihlášení na [gitlab.com](https://gitlab.com)
2. Vpravo nahoře zelené tlačítko **New project**
  ![GitLab new project](https://gitlab.com/Bulva/python-2020/raw/master/02-git_a_Gitlab/images/new_project.png)
3. Vyplníte název a dáte **Create project**


### Naklonování repozitáře (Clone)
Naklonování znamená "stažení" repozitáře do vašeho počítače (může být prázdný nebo může už obsahovat nějaké soubory). Zpravidla ho provedete jen jednou a pak už jen stahujete změny, které se v repozitáři udály. Pokud budete chtít repozitář znovu naklonovat musíte vymazat složku kde se repozitář naklonoval (obvykle `C:\Users\username\PycharmProjects\nazev_repozitare`)

#### Pomocí Pycharmu
1. V horním menu VCS -> Checkout from Version Control -> Git
2. Do okna Clone repository zkopírujete URL (protokol HTTPS) z vašeho repozitáře na GitLabu
  ![GitLab http url](https://gitlab.com/Bulva/python-2020/raw/master/02-git_a_Gitlab/images/project_url.png)
  ![Pycharm clone](https://gitlab.com/Bulva/python-2020/raw/master/02-git_a_Gitlab/images/clone.png)
3. Kliknete na tlačítko **Clone**. Na uvedené cestě by se vám měl naklonovat repozitář. Vytvoří se složka, která bude obsahovat další složku .git (bude skrytá).
4. Repozitář si můžete kdykoliv otevřít v Pycharmu - File -> Open a vyberete složku repozitáře.

#### Pomocí příkazové řádky
1. Otevřete příkazovou řádku a nastavíte si adresář na místo (pomocí `cd cesta`), kde chcete vytvořit složku z repozitářem.
2. Pustíte příkaz `git clone adresa_repozitare`, např. `git clone https://gitlab.com/Bulva/python-2020.git`.
  * měla by se vám vytvořit složka s naklonovaným repozitářem.


### Stáhnutí změn (Pull)
Pokud na repozitáři bude pracovat víc lidí, může se stát, že vaše lokální verze neobsahuje změny, které někdo odeslal do repozitáře. Pro aktualizaci slouží příkaz Pull. V našem případě se to týká jenom repozitáře **python-2020** kam vám můžu dát nějaké příklady nebo úkoly apod. Bylo by dobré tímto vždy začít hodinu, protože repozitář bude pravděpodobně obsahovat nějaké nové materiály.

#### Pomocí Pycharmu
1. Pravé kliknutí na název projektu (repozitáře) v levém okně Pycharmu (projekt musíte mít otevřený) -> Git -> Repository -> Pull

#### Pomocí příkazové řádky
1. Otevřete příkazovou řádku a nastavíte si adresář na místo (pomocí `cd cesta`) repozitáře (budete uvnitř repozitáře). Pokud máte repozitář python-2020 tak musíte dát `cd python-2020`.
2. Pustíte příkaz `git pull`


### Lokální uložení změn (Commit) a odeslání změn na server (Push)
Pokud upravíte kód uvnitř repozitáře (bude se v našem případě týkat jen vašeho repozitáře) a chcete tyto změny uložit. Ale pozor! Pouze lokálně!! Tzn. že změny se neukážou na GitLabu. Pouze se uloží, že jste provedli nějaké změny včetně zprávy, která změny bude popisovat. Tohle budete muset udělat pokáždé když budete odevzdávat úkol, písemku nebo si přidáte do repozitáře nějaký kód.

#### Pomocí Pycharmu
1. Pravé kliknutí na název projektu (repozitáře) v levém okně Pycharmu (projekt musíte mít otevřený) -> Git -> Commit Directory
2. V okně se vám zobrazí všechny změny v souborech co jste provedli.
3. Vložíte nějakou zprávu, která popisuje změny.
4. Dole kliknete na **Commit**. Pokud chcete změny rovnou přenést i na GitLab tak kliknete u tlačítka na šipku a **Commit and Push**. Pak dáte **Push**. Z pohledu gitu se provedou dvě operace. Nejdřív Commit a poté až Push.

#### Pomocí příkazové řádky
1. Otevřete příkazovou řádku a nastavíte si adresář na místo (pomocí `cd cesta`) repozitáře (budete uvnitř repozitáře). Pokud máte repozitář python-2020 tak musíte dát `cd python-2020`.
2. Pustíte příkaz `git status`. Zobrazí se vám výpis změněných souborů. Červené soubory nejsou zaznamenány pro změny. Pokud v nich chcete změny trackovat musíte je přídat
3. Přidáte je příkazem `git add soubor`, např. `git add test.py` nebo `git add ukol_1/test.py`. Při dalším puštění příkazu `git status` by měly soubory být zelené.
4. Když máte všechny soubory, které chcete trackovat přidané tak pustíte commit (viz krok 5)
5. Pustíte příkaz `git commit -m "nejaka zprava"`. Tento příkaz udělá lokální uložení změn včetně zpravý popisující změny.
6. Pokud chcete změny promítnout na GitLab tak pustíte příkaz `git push origin master`.





