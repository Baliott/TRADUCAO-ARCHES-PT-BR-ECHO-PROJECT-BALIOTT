label a1s1:
    $ quick_menu = False
    $ persistent.act_2 = False
    $ persistent.musicon = False
stop music fadeout 3.5
scene black
with transition_fade
show text "{size=70}Run{/size}" with medium_dissolve
pause 2.0
hide text with medium_dissolve
pause 1.0
play background reststop fadein 3.0
scene bg rural_road_day with medium_dissolve
pause 3.0
$ quick_menu = True
window show
"Corrida era algo em que ele sempre foi bom. Ele sempre foi o mais rápido da sua turma."
"Foi apenas no ano passado que ele ficou em segundo lugar nos 200 metros rasos no campeonato estadual."
"Faz apenas oito meses que um técnico da Universidade de Pueblo o abordou para entrar na equipe de atletismo após a formatura."
"Foi apenas no mês passado que ele percebeu que era o calouro mais rápido do time."
"Foi apenas na semana passada que ele começou a sair com homens mais velhos que podiam levá-lo aos bares gays de Pueblo."
stop background fadeout 10.0
play music2 soldering volume 0
play music solderingintro fadein 10.0 volume 0.3
queue music solderingloop volume 0.3
"Há apenas três dias, um desses homens drogou a sua bebida."
"Há apenas dois dias, ele acordou amarrado."
"Ontem mesmo, estava a ser torturado."
"Há apenas dez minutos, conseguiu escapar."
"Mas agora, ele percebe que isso não importa."
"Por todo o lado onde olha, só há deserto em chamas. Não há ninguém."
"As tentativas de gritar por ajuda valem ainda menos, porque a sua voz está destruída. Mal consegue chiar depois do que o homem lhe fez."
"E agora os seus sons vazios e arrastados são engolidos pelo deserto."
"Enquanto isso, os passos pesados arrastando-se pela gravilha atrás dele continuam a aproximar-se. O homem não tem pressa nenhuma."
"Correr era algo em que ele sempre foi bom."
"Mas agora, quando mais importa... ele não consegue."
"O caloiro mais rápido de uma universidade da Divisão 1 não é mais rápido do que um velho drogado."
"Ele teria sido, de certeza... se tivesse comido alguma coisa nos últimos três dias."
"Se não tivesse as costelas partidas. Se conseguisse ver direito."
"O homem deu-lhe algo. Disse que era para a dor, mas a dor continua lá, e agora ele nem sequer consegue ficar de pé."
"O equilíbrio foi-se, e ele tropeça sem parar até que só consegue rastejar de gatinhas."
"É aí que percebe que o homem o deixou fugir de propósito."
"E isso faz com que ele perceba outra coisa: vai morrer."
"Exausto da droga, dos últimos três dias de medo e tortura constantes, e de tentar fugir... ele colapsa."
"Fica ali, deitado na terra, a soluçar, mesmo sem lágrimas para chorar."
"Elas acabaram... depois de tudo o que o homem lhe fez."
window hide
pause 0.5
scene sunlight with sunlightright
pause 1.0
scene no_help_1 with medium_dissolve
pause 1.0
window show
"A luz por cima é ofuscante. Ele pergunta-se se isto é Deus."
"A mãe dele é uma católica devota, e mesmo que ele nunca tenha acreditado, promete a esta luz que se tornará um crente aqui e agora... se ela o salvar."
play sound steps
play sound2 steps
"Os passos a estalarem na gravilha aproximam-se cada vez mais."
unk2 "{cps=20}I... {w=0.4}need.{cps=4}..{/cps}{w=0.4} Está na hora de partir."
"A sua voz ainda está rouca e áspera."
"Os passos aproximam-se ainda mais."
unk2 "{cps=20}I... {w=0.4}have a.{cps=4}..{/cps}{w=0.4} enfrentar"
"Ouve-se uma gargalhada infantil e aguda."

window hide
pause 0.5
scene no_help_2 with medium_dissolve
pause 1.0
window show
unk "\"Acho que te acertei vezes demais. Agora só sabes falar da porcaria da tua pista.\""
"A forma enorme aproxima-se."
unk "\"Sabes que essa merda já não importa, certo?\""
"O peito dele dói de uma tristeza e desespero avassaladores. E não é só porque está prestes a morrer."
"É porque a mãe dele não vai saber o que lhe aconteceu."
"E é porque a última mensagem de texto que viu dela dizia \"Amo-te, insetinho!!!\" com dez emojis de corações e beijos."
"Na altura, ele só revirou os olhos e não respondeu."
"Achava que podia fazê-lo no dia seguinte, ou no outro."
"Depois de ter sido raptado, o homem tirou-lhe o telemóvel e colocou-o no balcão."
"Ficou ali, a vibrar vezes sem conta com mensagens, e o raptor só se ria quando ele pedia para, pelo menos, as ler."
"Agora as lágrimas escorrem, mesmo quando o homem se inclina sobre ele com algo pesado na pata."
"Ele espera que a mãe esteja certa sobre Deus."
"Espera poder vê-la do outro lado."
"Só para conseguir responder-lhe de alguma forma."
stop music
stop music2
scene bg black
centered "{cps=1}...{w=1.0}{nw}"
centertext "Mas há apenas..."
window hide
pause 2.0
play background highway fadein 5.0
scene bg outskirts_evening with medium_dissolve
pause 1.0
window show
"Cameron agarra-se ao banco com força, os dentes do coiote batendo uns nos outros a cada buraco que passam."
"O namorado dele, Devon, parece não se incomodar nada; a pata do urso no volante com o cotovelo pendurado pela janela."
"Tinha estado a cantar alto com a música que tocava nas colunas Bluetooth do carro, e só quando perderam sinal de rede é que Devon pareceu notar o desconforto de Cameron."
d "\"Estás bem, amor?\""
c "\"Acho que podias ir um bocadinho mais devagar.\""
d "\"O quê!?\""
"Cameron levanta a voz, gritando por cima do barulho do interior a tremer."
c "\"Mais devagar!\""
d "\"Porquê? Este é o tipo de terreno para o qual esta menina foi feita!\""
c "\"Está bem, mas--\""
"A voz de Cameron salta quando passam por mais uma valeta funda na estrada destruída."
c "\"Não sabemos o que está atrás de cada curva. E se de repente acaba e vamos parar a um desfiladeiro ou assim!?\""
d "\"É para isso que servem as barras de segurança, querido!\""
c "\"E estou prestes a partir um dente, de certeza!\""
d "\"Oh vá lá. Tens de admitir que há algo de bom em {i}sentir{/i} a estrada.\""
"Cameron não responde e continua agarrado ao banco."
"Devon abrandou um pouco, manobrando com mais cuidado pelas partes mais partidas da estrada."
c "\"O que aconteceu à estrada afinal? Só passaram o quê, cinco anos?\""
d "\"Cheias repentinas, pelo que li online... Obviamente ninguém faz manutenção, então dá nisto.\""
c "\"Ah pois, esqueci-me como este estado funciona; seco como tudo até cair uma parede de água durante a época das monções.\""
"O coiote fica tenso quando o urso faz outra curva suave mas ainda assim repentina."
c "\"E está ainda mais quente do que me lembrava.\""
d "\"Como é que és um coiote, Cameron? Este é o teu clima!\""
c "\"Sabes que não deves dizer isso. Só porque fui feito para isto não quer dizer que tenha de gostar.\""
d "\"Yeah, yeah, mas também odeias Fort Allen.\""
c "\"Lá não fica INFERNALMENTE quente. Consigo aguentar.\""
d "\"Bem, a transferência para Bonneville City está bem encaminhada, por isso não vais ter de aguentar muito mais.\""
"Cameron encolhe os ombros."
c "\"Tempo mais ameno até era bom, acho.\""
"Devon sorri."
d "\"Tempo melhor, {w=0.3}paisagem melhor, {w=0.3}e pessoas melhores.\""
c "\"Toda a gente é mórmon.\""
d "\"É por isso que são simpáticos!\""
c "\"Os que vivem aqui em baixo não são.\""
d "\"Há uma GRANDE diferença entre os fundamentalistas e os--\""
c "\"Normais?{w=0.3} Os que batizam mortos e usam pijamas de Jesus debaixo da roupa?\""
"Dev encolhe os ombros."
d "\"A maioria das religiões é estranha quando as analisamos assim.\""
c "\"Só estou a dizer, sejam roupas mágicas ou vestidos de pradaria, vieram do mesmo sítio lixado.\""
"Devon não diz nada, e Cameron apercebe-se de como está a soar mal neste momento."
c "\"Desculpa, só me preocupo com a forma como nos podem ver. É mais difícil perceber quem são quando são todos falsamente simpáticos.\""
d "\"Yeah, isso é verdade, mas olha--\""
"Dev acena com a cabeça em direção à janela de Cameron, e o coiote segue o olhar dele."
"A paisagem rochosa e irregular abriu-se para uma vasta extensão azul."
d "\"É o Lago Emma, {w=0.3}o que significa que Echo está--\""
"O urso olha para a frente, e a primeira coisa que Cameron vê é um letreiro alto e enferrujado com letras no topo que não consegue ler bem àquela distância."
"Por baixo está um edifício pequeno e degradado, e além dele há outros ainda mais pequenos e em pior estado."
"Cameron não sabia bem o que ia sentir ao ver a cidade pela primeira vez."
"Se o coiote é mesmo o que Devon pensa, então agora estaria a sentir todas as coisas horríveis e más que supostamente aconteceram ali."
"Aqueles edifícios pequenos e degradados deviam exalar as memórias do passado, que seriam então projetadas na mente dele."
"Mas Cameron sente.{cps=3}.. {/cps}{w=0.3}nada."
"Claro que, no fundo, ele já esperava isso, mas nunca tinha estado num sítio conhecido por ser assombrado."
"Pelo menos não como Echo."
"Por isso estava um bocadinho preocupado."
"Dev já lhe tinha pedido no passado para o acompanhar nas suas \"investigações paranormais\" de amador."
"Tudo porque o coiote conseguia \"ver\" coisas."
"Ele lembrava o Dev que a palavra certa era \"alucinar\"."
"As coisas que via eram manifestadas pela sua própria mente."
"Não havia razão para alimentar isso indo a um sítio supostamente assombrado."
"Dev percebeu a mensagem rapidamente e deixou de pedir."
"Mas continuaram a falar sobre esses interesses, e Cameron percebeu que havia muito mais no interesse de Devon por fantasmas do que apenas diversão estúpida."
"E mesmo tendo recusado alimentar o disparate psíquico de Devon, o urso continuou a cuidar dele."
"Fez tanto pelo coiote que Cameron até se sentia envergonhado ao pensar nisso às vezes."
"Por isso, quando Dev teve esta oportunidade de ir ao sítio onde sempre quis ir, Cameron decidiu que também tinha de ir."
"Está a fazer isto por Dev, para mostrar gratidão por tudo o que ele fez por si."
"Mesmo assim, Devon tentava tornar isto mais como umas férias, como se Cameron não fosse fazer investigação nenhuma."
"Ele teria de falar com o urso e dizer-lhe que estava disposto a levar isto a sério, pelo menos dentro do razoável."
"Também precisava de lhe dizer porque é que não gostava de fazer isto, e essa parte ia ser difícil."
c "\"Não parece assim tão má, para uma cidade fantasma, digo.\""
d "\"As aparências iludem. Espera aí. Tenho de parar por um momento.\""
c "\"Porquê?\""
d "\"Quero espreitar o lago antes de escurecer, e também preciso de fazer um {i}enooooorme{/i} xixi.\""
"Cameron tenta não suspirar, só querendo entrar na cidade para ter a certeza de que não sente nada."
"Para realmente garantir que não há nada com que se preocupar."
"Ele não está preocupado com fantasmas, mas sim com o seu próprio cérebro e o que este possa fazer."
"A estrada torna-se mais lisa e com aspeto mais recente à medida que chegam junto ao lago."
window hide
play sound engineoff
pause 0.5
scene black with leftwipe
pause 0.5
scene bg lakeside_evening with leftwipe
stop background fadeout 5.0
pause 1.0
window show
d "\"Eles estavam a tentar transformar este reservatório num local de lazer mesmo quando tudo aconteceu.\""
play sound cardoor
"Ambos saem do carro, Cameron a esticar as pernas com gratidão."
window hide
pause 0.5
play music2 roadside volume 0
play music roadsideintro volume 0.3
queue music roadsideloop volume 0.3
show cam serious c evening at right with Dissolve(1.5)
pause 0.5
window show
c "\"Que pena. Até parece giro.\""
show dev h evening at left with dissolve
d "\"Sim, este lugar tem tido uma maré de azar atrás de outra.\""
c "\"'Maré de azar' é uma maneira de dizer--\""
show dev happy evening with dis
d "\"Espera aí, {w=0.3}tenho de ir fazer xixi!\""
hide dev with dissolve
show cam annoyed a evening with dis
"O Dev vai a andar apressado, claramente já não aguentava mais."
"O Cameron abana a cabeça, a lembrar-se de todas as áreas de descanso que passaram na autoestrada."
show cam disappointed evening with dis
"Com um suspiro, Cameron encosta-se ao Jeep, a olhar para o lago."
"Até agora isto nem é nada mau."
"Claro, ainda não estão na vila, mas todos aqueles sonhos, aqueles sentimentos horríveis... Agora parecem parvos."
"É só uma vila pequena, com uma história triste."
"Se o cérebro dele fosse manifestar alguma coisa disto, seria só... tristeza."
"O Cameron sabe que as alucinações não são reais. Ele sabe isso desde pequeno, depois de ver um monstro com uma gabardina na caravana onde vivia."
"Também sabe que fantasmas não existem."
"Mas o Devon acredita. Ou pelo menos quer acreditar."
"Quer tanto, e pensa que o Cameron os consegue ver."
"O Cameron sabe que há algo mesmo errado em usar uma possível doença assim."
"O Devon também sabe. {i}Sabe bem demais.{/i}"
"Ao ponto de o Cameron conseguir prever, dias antes, que ele ia perguntar se podiam fazer esta viagem."
"E sim, isto está errado. Mas o urso nem acha que o Cameron tenha uma doença mental, pelo menos é o que parece ao coiote."
"O Devon não percebe o que é lutar com a realidade, ter estes problemas e nunca receber um diagnóstico certo."
"O Cameron só sabe que algo está errado, e sempre esteve."
"E, além disso, nunca contou bem como era. Então como é que o Devon ia entender?"
"Contou um bocadinho, mas tinha sempre aquele medo no fundo que o Dev fosse embora se soubesse tudo."
"Então o Dev pegou nesses pedacinhos e achou que o Cameron era \"dotado\"."
"Ele não o podia culpar; às vezes o que ele vê parece mesmo ter um significado mais profundo, como se houvesse algo além da saúde mental."
"Mas isso não é exatamente o que acontece com várias doenças mentais? Não se reconhece o que é real?"
"Já passaram mais de cinco anos, e o Dev viu o Cameron no pior — no ponto mais louco — e mesmo assim ficou, ainda acreditando que o Cameron era só um rapaz normal com problemas pessoais."
"O Cameron abraça-se mais um bocadinho, a perceber que agora é o momento para falar mesmo a sério."
"E depois disto, podem começar de novo em Bonneville."
show dev smirk p evening at five behind cam with dissolve
d "\"Phew, {w=0.3}sinto-me pelo menos um quilo e meio mais leve depois disto.\""
show cam unamused c evening with dis
c "\"Sabes, eu não me importo de fazer xixi na natureza, mas mais do que isso não faço.\""
show dev embarrassed evening with dis
d "\"Yeah, eu estava com esperanças que houvesse uma casinha-de-banho ou duas por aqui, mas parece que vamos ter de cavar buracos--\""
show cam angry evening at jumping
c "\"DEV!\""
show dev scream evening at jumping
d "\"Whoa! {w=0.3}Estava só a brincar, amor!\""
show dev grin p evening with dis
d "\"Podemos ir até à próxima área de descanso.\""
show cam disgusted evening with dis
c "\"Hmph.\""
show dev shocked h evening with dis
d "\"O que foi?\""
"O coiote faz uma pausa, a tentar preparar-se para a conversa desconfortável que vem aí."
show cam disappointed evening with dis
c "\"Uh.{cps=3}..{/cps}{w=0.4} Dá-me só um segundo.\""
stop music fadeout 10.0
stop music2
play background lakesounds fadein 5.0
"O Cameron vê logo que o urso muda de atitude."
show dev embarrassed evening with dis
d "\"O-Okay.{w=0.3} Um, {w=0.3}mas enquanto te dou esse segundo, {w=0.3}desculpa por estar a brincar e ser nojento.\""
show dev disappointed evening with dis
d "\"Eu sei que isto não é bem onde querias estar agora, e só estava a tentar animar as coisas, e sabes que é porque te amo--\""
show cam frustrated evening with dis
c "\"Jesus Cristo, {w=0.3}pára!\""
show dev embarrassed evening with dis
"O Devon fica calado e engole em seco, o som alto quase parece cómico."
"Há uma pausa, e embora o Cameron tente manter-se sério, a tensão quebra-se sozinha."
show cam happy eyes evening with dis
c "\"Prefiro muito mais ouvir-te fazer piadas sobre cocó do que ver-te assim. É tão estranho.\""
show dev skeptical p evening with dis
d "\"O quê, {w=0.3}ser atencioso?\""
show cam smirk c evening with dis
c "\"Mais ou menos. És atencioso, só que não daquela maneira estranha e ansiosa.\""
show dev shocked p evening with dis
d "\"Bem, processa-me por tentar ser cuidadoso. Só não quero dizer algo estúpido e--\""
"Cameron interrompe o urso, sem querer adiar mais isto."
show cam worried a evening with dis
c "\"Devon, ouve-me só um minuto.\""
c "\"Eu sei que não disseste nada, mas vamos ser diretos e admitir que ambos sabemos que estou aqui por mais do que companhia. Não sou assim tão estúpido.\""
show dev disappointed evening with dis
d "\"Ah...\""
show cam worried a evening with dis
c "\"E só quero dizer que não acho que isto seja uma boa ideia porque o que eu tenho é... algum tipo de problema, não uma habilidade--\""
show dev surprised p evening with dis
d "\"Eu sei, não devia pensar assim, mas pesquisei e simplesmente não me parece que se alinhe com teres uma doença ment--\""
show cam frustrated evening with dis
"Devon cala-se quando Cameron suspira profundamente."
c "\"Por favor, {w=0.3}não.\""
show dev embarrassed evening with dis
d "\"Descul--\""
"Devon interrompe-se desta vez, tentando esconder uma careta."
show cam worried a evening with dis
c "\"Quer dizer, tens razão que não sabemos exatamente qual é o meu problema. Só sei que não é bom--\""
c "\"--mas o que importa é se isto te ajuda a {i}ti{/i}, quer eu ache que é real ou não. Fizeste muito por mim, e quero poder fazer algo por ti.\""
show dev skeptical p evening with dis
d "\"Não, o que eu acho não importa. O mais importante é--\""
c "\"ENTÃO, {w=0.3}vou fazê-lo. {w=0.5}Vou ser o teu médium este fim de semana.\""
show dev shocked h evening with dis
d "\"Espera, {w=0.3}sério?\""
show cam annoyed evening with dis
c "\"Dev, não vou passar o tempo todo a fingir que estamos a ter um tempo bom e inocente naquela cidade de assassinatos.\""
d "\"Mas.{cps=3}..{/cps}{w=0.4} Eu não quero obrigar-te a fazer algo que não--\""
show cam smile c l evening with dis
c "\"Oh, eu quero. Pode ser que não {i}goste{/i}, mas quero fazê-lo. Nem que seja só por ti.\""
show dev embarrassed evening with dis
d "\"Cam--\""
c "\"Nada disso, já tomei a minha decisão, e vou fazê-lo. Mas só desta vez.\""
show dev worried p evening with dis
d "\"Se tens a certeza, mas por favor não me ponhas à frente de t--\""
show cam smile talking c evening with dis
c "\"E fiz alguma pesquisa naquele fórum que me enviaste há uns anos, por isso o meu sexto sentido está afinado e pronto.\""
"Isso parece finalmente tirar Devon da sua relutância, e um pouco da irritação por estar a ser constantemente interrompido."
show dev happy evening with dis
d "\"Espera, {w=0.3}sério!? {w=0.4}Havia tantas pessoas como tu nesse fórum. Tu--\""
show cam serious c evening with dis
c "{i}\"Escuta{/i}. Quero mesmo que encontres as tuas respostas, MESMO, mas acho que a pior coisa que podia fazer era mentir para te fazer sentir melhor. Vou ser completamente honesto sobre tudo--\""
show cam disappointed evening with dis
"Cameron encosta-se ao jipe."
c "\"--quer veja alguma coisa ou não.\""
show dev h evening with dis
d "\"Claro, é isso que eu quero!\""
c "\"E é por isso que não devias estar a criar grandes expectativas agora. Só te estou a dizer que vou tentar.\""
show dev smirk h evening with dis
"O urso fica a olhar para o Cameron durante alguns segundos, apenas a sorrir."
show cam confused a evening with dis
c "\"...O quê?\""
show dev grin h evening with dis
d "\"Só estou feliz por te ter conhecido, {w=0.3}por estarmos juntos, {w=0.3}e por estares aqui comigo.\""
"Devon passa um braço à volta de Cameron, puxando-o para junto de si enquanto também se encosta ao jipe."
window hide
pause 0.5
$ renpy.music.set_volume(0.2, delay=3, channel=u'background')
play music2 unfold volume 0
play music unfoldintro fadein 10.0 volume 0.3
queue music unfoldloop volume 0.3
scene lake_emma_1
show lake_emma_1
show lake_emma_2
show lake_emma_3
with medium_dissolve
pause 1.0
window show
d "\"Mas a sério, {w=0.3}se alguma vez sentires que.{cps=3}..{/cps}{w=0.4} sei lá, {w=0.3}que já não estás para isso, diz-me.\""
c "\"Bem, desde que não estejas à espera de nada, acho que vai correr bem.\""
d "\"Yeah.\""
"Devon continua a sorrir e Cameron estreita os olhos."
c "\"Porque estou a ter a sensação de que estás à espera de muita coisa.\""
"Devon pausa, parecendo pensar."
d "\"Bem, também estou feliz por estares a ser mais aberto assim. Sempre senti que não querias falar sobre isso.\""
"Cameron também pensa."
scene lake_emma_2 with dis2
c "\"Acho que só não queria que me dissessem que o que vejo tem de {i}significar{/i} alguma coisa, percebes?\""
d "\"Yeah, isso deve cansar rápido, mas já que estamos a falar sobre isso agora--\""
d "\"--não significa mesmo? Tipo, algumas das coisas que mencionaste não fazem sentido, como aquela criatura do impermeável, mas e o teu velho amigo que... ya sabes?\""
c "\"Levou um tiro na cabeça? Depois de eu ter alucinado que alguém lhe dava um tiro na cabeça?\""
d "\"Uh, {w=0.3}yeah, {w=0.4}esse.\""
c "\"É disso que estou a falar. Tu, e todos nós, gostamos de ver significado em tudo.\""
c "\"Achamos que temos um propósito na vida, {w=0.3}uma {i}razão{/i}.\""
c "\"Razão, {w=0.3}propósito, {w=0.3}e o sentido da vida não significam nada para o universo.\""
c "\"Tudo simplesmente {i}é{/i}. Se tem significado ou não, depende de nós.\""
c "\"Sim, é estranho que eu tenha alucinado a forma como ele iria morrer, mas ele também estava envolvido em coisas que podiam levar a isso.\""
c "\"Eu sabia que ele andava a traficar drogas de forma muito arriscada, por isso sabia que a vida dele estava em perigo, {i}e{/i} eu estava sob o efeito de ketamina. Toda a lógica está lá.\""
d "\"Bem, {w=0.3}eu, {w=0.3}uh--\""
"Devon mexe-se desconfortável, claramente a tentar disfarçar."
d "\"Percebo isso, mas há muitos outros exemplos que podia mencionar. Pode ser coincidência, mas a certa altura não tens de te perguntar se talvez seja outra coisa?\""
"Cameron suspira."
c "\"Claro que já me perguntei, mas o que sempre me assusta nestas coisas do paranormal em que estás metido, e na vida depois da morte e isso tudo--\""
scene lake_emma_3 with dis2
c "\"--faz-me lembrar a minha mãe.\""
"Devon não diz nada, apenas espera e ouve."
c "\"Sabes, no fim, mesmo antes de eu sair, ela andava sempre sob o efeito de alguma coisa para se manter acordada com os três trabalhos que tinha, fossem anfetaminas ou metanfetaminas, quase não dormia.\""
c "\"Tínhamos uma ventoinha no nosso atrelado, e um dia, depois de a ligar, perguntou-me se eu conseguia ouvir alguém a falar {i}através{/i} da ventoinha.\""
"Cameron tinha pensado se devia ou não contar a Devon todos os detalhes sobre a mãe, mas sente que tem de o fazer."
"Nem que seja para que Devon tenha uma explicação do porquê."
c "\"Eu disse que não, mas ela sentou-se ao lado e ficou a ouvir, e eventualmente teve uma enorme epifania de que era Deus.\""
c "\"E fez isso durante semanas, e era praticamente tudo o que fazia quando estava em casa; ouvir a ventoinha a falar com ela.\""
c "\"Não sei ao certo o que lhe dizia. Nem acho que percebia mesmo o que se passava.\""
c "\"Só sabia que às vezes os toxicodependentes fazem esse tipo de cenas, especialmente quando não dormem, percebes?\""
c "\"Mas depois começou a procurar formas específicas; arcos e meias-luas.\""
c "\"Essa voz disse-lhe que podia entrar no céu se passasse pelo arco certo.\""
c "\"Mas a voz também disse que o diabo a ia tentar enganar com falsos para tornar o 'verdadeiro' mais difícil de encontrar.\""
c "\"Ela apontava-mos, dizia-me como havia tantos, e sim, eles estavam lá, mas quando procuras esses padrões, por algo tão simples como a forma de um arco--\""
"Cameron passa o dedo ao longo do arco da roda onde está encostado."
c "\"--vais encontrá-los.\""
c "\"Eventualmente, disse-me que tudo estava distorcido. Acho que estava tão lixada que estas formas simplesmente se destacavam, como se o cérebro dela as iluminasse e ela não conseguisse ignorá-las.\""
c "\"No último dia, disse-me que até {i}eu{/i} parecia um arco, e que achava que eu tinha sido condenado ao inferno.\""
c "\"Ela parecia completamente.{cps=3}..{/cps}{w=0.4} esgotada.\""
c "\"Disse-me que voltaria para me salvar, e depois saiu do atrelado.\""
c "\"Umas horas depois, afogou-se a tentar nadar por baixo de uma ponte, e toda a gente no parque de caravanas viu aquilo como apenas mais uma toxicodependente iludida que acabou por se matar acidentalmente.\""
"Cameron tinha dito a Devon que a mãe se afogou num rio enquanto estava sob o efeito das drogas, mas os detalhes são arrepiantes, e o urso apenas o abraça mais apertado."
c "\"Mas eu acho que foi suicídio, que ela estava tão farta da vida de merda que tinha que apostou naquela ponte ser o arco que a levaria ao céu, de uma forma ou de outra.\""
scene black
show lake_emma_2
with dis2
c "\"Por isso é que me preocupo em seguir estes padrões, mesmo que seja só algo como procurar OVNIs ou fantasmas.\""
c "\"Tipo, sim, a metanfetamina e a falta de sono a empurraram para o limite, mas será que há algo genético também?\""
c "\"O meu pai também teve problemas.\""
c "\"E se eu estiver predisposto a isso? Eu achava que as drogas estavam a piorar, mas não uso desde o segundo mês depois de te conhecer, e ainda vejo coisas de vez em quando.\""
scene lake_emma_3 with dis2
c "\"Eu quero dizer, seja o que for que se passa comigo, está estável, mas fico a pensar se isso vai durar.\""
"Devon limpa a garganta."
d "\"Eu {i}nunca{/i} deixaria isso acontecer contigo. Sei que digo coisas estúpidas sobre isso, mas sei que pode ser perigoso, e estou sempre a olhar por ti.\""
scene lake_emma_2 with dis2
c "\"Sinceramente, é bom ouvir isso, porque deixar a minha mãe sentar ao lado de um ventilador durante três horas seguidas todos os dias, alimentando as suas ilusões, foi a coisa mais estúpida que eu já fiz.\""
c "\"Mas eu estava viciado na minha própria droga de eleição porque simplesmente não me importava. Mas o que acontece é que, mesmo naquele inferno em que ela estava, {i}ela{/i} se importava.\""
c "\"Tomei demasiado umas quantas vezes, e mesmo que ela estivesse a ouvir o ventilador, no seu próprio mundo, a colar post-its nas formas que via--\""
c "\"--ela percebeu logo quando a minha respiração não estava certa, e acordei com ela a pulverizar Narcan no meu nariz.\""
"Cameron vê Devon a inclinar a cabeça, questionando."
c "\"Isso anula uma overdose de opióides.\""
scene lake_emma_3 with dis2
c "\"Mas a questão é que, {w=0.4}a minha mãe não gostava de opióides porque a faziam sentir-se enjoada.\""
c "\"Então isso significa que ela arranjou esses sprays nasais só para mim, só por precaução, mesmo quando eu pensava que ela estava demasiado absorvida no seu próprio mundo para se importar.\""
c "\"Por isso, dói pensar naquela noite, como eu simplesmente a deixei sair da nossa carrinha assim.\""
window hide
pause 0.5
stop music fadeout 7.0
stop music2
$ renpy.music.set_volume(1.0, delay=5, channel=u'background')
scene bg lakeside_evening with medium_dissolve
pause 0.5
window show
"Cameron respira fundo novamente."
"Ele não tinha planeado falar sobre essa última parte, mas simplesmente saiu."
show cam sad evening at right with dissolve
c "\"{cps=30}Desculpa, {w=0.3}não estava mesmo a planear contar tudo isso.\""
show dev embarrassed evening at left with dissolve
d "\"Amigo, {w=0.3}não te preocupes.\""
show cam disappointed evening with dis
c "\"Mas é parte do motivo de eu ser como sou. Sei que os meus sintomas não correspondem perfeitamente ao que pesquisaste na internet, mas estão perto o suficiente.\""
c "\"E sinceramente, talvez tenhas razão, talvez haja algo depois de morrermos, e de alguma forma posso ajudar-te a encontrar isso, mas se as coisas correrem mal, e se houver algo errado comigo, só me traz de volta.\""
show cam worried a evening with dis
c "\"Ver a forma de um arco, lembrar-me de todos os marcadores que ela pôs neles, é como um lembrete do que aconteceu com ela e o que pode acontecer comigo.\""
hide dev
hide cam
with dissolve
"Silenciosamente, Devon puxa Cameron para um abraço, e o coiote encosta a cabeça ao peito dele."
"Neste momento, Cameron percebe então porque é que tantas pessoas adoram os seus terapeutas."
"Ele sempre se preocupou que Devon se assustasse com o que aconteceu quando era mais jovem."
"Que finalmente veria todos os esqueletos no seu armário: negligente, negligenciado, abusivo, abusado, e tão desesperadamente viciado."
"Tal como a mãe dele. A definição de lixo de trailer."
"Cameron foi tudo isso em algum momento da sua vida, mas sabe que isso não importa para Devon."
window hide
stop background fadeout 6.0
pause 0.5
scene black with leftwipe
pause 0.5
play ambient desertmorning fadein 10.0
scene bg outskirts_evening with leftwipe
pause 0.5
window show
"Depois de algum tempo, Devon solta-o e começam a voltar para o Jeep, o urso a sentir-se ligeiramente nervoso."
"Abrir-se como Cameron fez agora tinha sido verdadeiramente aterrador."
"Devon soubera algumas partes da história do coiote, mas ouvir tudo assim, como ele quase teve uma overdose e... "
"Dev dá um arrepio."
"Está apenas feliz por o coiote estar seguro com ele agora, fora daquele inferno."
"Quando está prestes a entrar no seu lado do Jeep, ele olha para a cidade, que fica a apenas uma milha de distância."
"Enquanto Cameron lhe disse que isso tudo o fez sentir-se melhor, Devon estava mais confuso do que nunca."
"Tudo o que Cameron lhe contou praticamente gritava que isso era uma má ideia, que isso não era bom para ele."
"Será que importa o que {i}ele{/i} pensa sobre as alucinações de Cam?"
"Que a pesquisa superficial dele sobre psicologia anormal, especialmente sobre alucinações, o levava a crer que Cameron não estava mentalmente doente?"
"Não."
"Como poderia ele levá-lo a Echo depois de ouvir isso?"
"Como poderia arrastá-lo para esta busca interminável pela verdade outra vez?"
"Mas, ao mesmo tempo, Cameron está a dizer-lhe que quer fazer isso."
"Dev olha para o capô do Jeep, batendo as garras cegas no topo macio."
show dev grin p evening at left with dissolve
d "\"Ei Cam? Que achas de continuarmos para norte, dar uma vista de olhos em Deseret? Sabes, ver como é Bonneville. Ver como são os Mórmons. Isso pode ser divertido.\""
"Enquanto diz isso, há uma sensação esmagadora no seu peito, temendo que Cameron diga que sim, mas ao mesmo tempo, esperando que ele diga."
show dev worried p evening with dis
d "\"Quero dizer, com a forma como as coisas estão, nem sei se conseguiremos atravessar as fronteiras estaduais dentro de umas semanas. Estão a começar a fechar tudo.\""
"Mas Cameron olha para ele antes de esboçar um sorriso."
show cam smirk c evening at right with dissolve
c "\"Oh não, {w=0.3}isto é algo que tu querias fazer há anos.\""
show cam smile evening with dis
c "\"Quero dizer, foda-se por te largar tudo isso AGORA antes de chegarmos lá, mas sabes que sou um procrastinador.\""
c "\"Não quero que te sintas culpado, mas apenas toma atenção.\""
c "\"E eu meio que quero enfrentar os meus medos de uma forma, sabes? Estou pronto para isso.\""
hide cam with dissolve
play sound cardoor
"E antes que Devon possa dizer mais alguma coisa, Cameron entra."
show dev embarrassed evening with dis
"Dev olha para o lago, realmente não sabendo o que está prestes a fazer."
"Se fosse um bom namorado, deveria ter saído desse lugar."
"Cameron gritaria, xingaria e reclamaria sobre como lhes levou dez horas a chegar lá."
"E Devon calaria-o com uma dessas abominações açucaradas do Starbucks."
"E nunca mais falaria sobre Echo."
"Ele ouviria Cameron e confiaria nele sobre como realmente era ver coisas terríveis."
"Fugiriam, casariam, comprariam uma casa grande, e mais cedo ou mais tarde, Dev teria a sua resposta, porque todos a têm no final."
hide dev with dissolve
"Quando saem do parque de estacionamento, ele pensa que tomou a sua decisão."
"Mas mesmo enquanto se diz a si mesmo que vai virar à esquerda, voltar pelo caminho por onde vieram--"
"Ele vira à direita."
stop ambient fadeout 3.0
"Porque antes de o fazer, vê um flash de rosa na sua mente, flutuando no meio de um lago, e é como se alguém lhe tivesse dado um soco no peito."
"Antes de perceber, Echo está à frente deles."
window hide
pause 0.5
scene black with medium_dissolve
pause 1.0
play ambient desertmorning fadein 6.0
scene bg motel_afternoon with medium_dissolve
pause 0.5
window show
"Devon franze a cara enquanto entra no parque de estacionamento do motel, a olhar para as paredes cobertas de grafite."
"As caricaturas de desenho animado têm uma maneira de desvalorizar esta experiência, como se fosse apenas uma atração estúpida de casa assombrada."
stop ambient fadeout 10.0
play music2 monochrome volume 0
play music monochromeintro fadein 3.0 volume 0.3
queue music monochromeloop volume 0.3
$ renpy.music.set_volume(0.5, delay=3, channel=u'background')
show cam worried a sunset at right with dissolve
c "\"Então este é o 'ponto de base', huh?\""
"Devon esfrega a parte de trás da cabeça, sentindo-se inseguro depois de ter falado tanto sobre este lugar."
show dev worried p sunset at left with dissolve
d "\"Não parecia {i}assim{/i} nas fotos.\""
show dev upset p sunset with dis
d "\"As pessoas nunca têm respeito por coisas como esta.\""
show cam smile a l sunset with dis
c "\"Eu não acho que pareça mau. Adoro arte de rua como esta.\""
show cam smile c l sunset with dis
c "\"E isso faz-me sentir menos sozinho, como se muita gente já tivesse estado aqui e tivesse ficado bem.\""
show dev annoyed p sunset with dis
d "\"Na verdade, fica de olho caso algum deles esteja à solta por aqui.\""
show cam serious a l sunset with dis
c "\"Todos os artistas de grafite que conheci eram muito fixes.\""
show dev serious h sunset with dis
d "\"Não é {i}fixe{/i} fazer isso num lugar onde muita gente morreu.\""
show cam smirk c sunset with dis
c "\"Bem, eu acho que muita gente não ia gostar do que {i}nós{/i} estamos a fazer, e sei que {i}tu{/i} és fixe.\""
show cam smile talking c sunset with dis
c "\"Então.{cps=3}..{/cps}{w=0.4} descontrai um bocadinho.\""
hide cam with dissolve
play sound slap
show dev shocked h sunset at jumping
d "\"Ai! {w=0.3}Que dor...\""
"Cameron passa por Devon, dando-lhe um estalo forte na bunda enquanto passa."
show dev skeptical p sunset with dis
"Devon levanta uma sobrancelha, não sabendo bem o que fazer com o bom humor de Cameron."
"Eles acabaram de ter uma das conversas mais pesadas da sua relação e..."
show dev h sunset with dis
"{i}...Bem, talvez isso seja {i}porquê.{/i}"
"Se Cameron se sentia mais confortável a ser honesto e aberto com Dev, então isso só pode ser uma coisa boa na cabeça do urso."
hide dev with dissolve
"Depois de devolver um estalo muito mais forte, que faz Cameron gritar, o urso junta-se a ele a explorar a área."
"Considerando que o motel deveria ser o edifício mais assombrado de Echo, Dev achou que seria uma boa ideia estabelecer a base ali."
"Especificamente no quarto 12, mas a maioria dos números estão faltando, e a maioria das portas metálicas pesadas estão trancadas."
"Mesmo que todas estejam amassadas, como se tivessem sido batidas por autênticos aríetes."
show dev upset h sunset at left with dissolve
d "\"Bem, eles realmente se importam em vedar o lugar.\""
show cam smile a l sunset at right with dissolve
c "\"Provavelmente cansaram-se dos idiotas a entrarem e a ficarem feridos.\""
show dev grin h sunset with dis
d "\"Sim, mas felizmente eu não sou um idiota.\""
show cam smile c l sunset with dis
c "\"Ei, e eu?\""
show dev smirk p sunset with dis
d "\"Bem, não acho que um diploma em música nos ajude muito nesta situação, mas ainda és bastante inteligente.\""
show cam unamused c sunset with dis
".{cps=2}..{w=0.7}{nw}"
show cam confused c sunset with dis
c "\"Ah merda, {w=0.3}é verdade! {w=0.4}Tu tiraste engenharia mecânica e trabalhas na empresa mais valiosa de automação industrial do país.\""
show dev worried h sunset with dis
d "\"Heh, sim.\""
"Devon está um pouco surpreso com a frieza da resposta de Cameron."
show cam unamused c sunset with dis
c "\"Bem, {w=0.3}vai lá. {w=0.3}As tuas aulas de dinâmicas e física baseada em cálculos devem resolver isso para nós.\""
"A voz de Cameron transborda sarcasmo, e Dev só pode assumir que está a gozar com a forma como o urso tentou impressioná-lo com os seus cursos durante os primeiros encontros."
"Mas Devon tenta salvar o bom humor que tiveram mais cedo."
show dev grin h sunset with dis
d "\"Bem, eu provavelmente conseguiria partir essas tábuas, desde que mova o meu punho a uma alta velocidade. Vês, a quantidade de energia cinética--\""
window hide
stop music2
stop music fadeout 10.0
pause 0.5
$ renpy.music.set_volume(1.0, delay=10, channel=u'background')
hide cam with dissolve
pause 1.0
show dev disappointed sunset with dis
window hide
pause 0.5
window show
play background desertmorning fadein 10.0
"Os comentários de Dev, que eram apenas provocações desinteressadas, vão-se esgotando."
"Ele nunca gostou muito do desprezo descarado que os seus colegas de STEM tinham pelas artes e ciências sociais."
"É só que isso irritava o Cameron, e isso era engraçado--"
"--na faculdade."
"Agora, o Devon sente-se um idiota."
"Além disso, a habilidade de Cameron para compreender e tocar música é basicamente mágica para o urso. A compreensão de Devon sobre música é superficial, e ele é ligeiramente surdo ao tom."
"O Cameron nunca apontaria isso, ele apenas cantaria e tentaria harmonizar."
"E embora Devon tivesse sido oferecido o seu salário de seis dígitos antes de se formar, ele viu os sonhos de Cameron de trabalhar na indústria musical evaporarem lentamente nos últimos três anos."
"Agora, Cameron trabalha numa central de atendimento que odeia."
show dev embarrassed sunset with dis
"O urso achava-se tão inteligente na faculdade, e sim, até se saía bem--"
"--mas agora ele está mais consciente de que é um estúpido quando se trata de comunicar com pessoas reais, com o seu namorado literal."
"Ele precisa pedir desculpa por isto."
"O urso limpa a garganta."
show dev grin p sunset with dis
d "\"Yo, Cam.\""
"Dev aproxima-se do coyote, mas antes de dizer algo, Cameron apenas aponta para uma porta."
show cam smile a sunset at right with dissolve
c "\"Vês? O número 8. E a porta ali é o número 3.\""
c "\"Então, contando nesta direção--\""
"A atitude fria de Cameron desaparece completamente."
show dev skeptical p sunset with dis
c "\"Dez, onze, e o quarto número 12. E não é que está aberto!\""
show dev happy sunset at left with dis
d "\"Ah, ótimo!\""
show cam grinning c l sunset with dis
c "\"Obrigado, eu fui à faculdade.\""
show dev smirk p sunset with dis
d "\"Ha-ha.\""
show dev skeptical p sunset with dis
d "\"Agora, eu vou entrar primeiro para garantir que está tudo claro.\""
show cam unamused a sunset with dis
c "\"De quê?\""
d "\"Não sei, {w=0.3}ocupantes ilegais?\""
show cam serious c l sunset with dis
c "\"Bem, prepara-te para encontrar um ocupante ilegal morto, porque como é que ele sobreviveria?\""
show dev surprised h sunset with dis
d "\"Na verdade, acabaste de me lembrar que há uns tipos esquisitos que vivem aqui, como locais teimosos que não querem sair. Pelo menos foi isso que um post disse, de há dois anos atrás.\""
show cam worried a sunset with dis
c "\"O quê? Não gosto de ouvir isso. Eles são perigosos?\""
d "\"Pelo que percebi, eles são mais do tipo 'sai do meu jardim'.\""
c "\"Esses tipos também podem ser perigosos.\""
show dev p sunset with dis
d "\"Se ninguém morreu por causa deles até agora, então acho que estamos bem, mas como disse: vou olhar por ti.\""
"Dev solta um rosnado falso."
show dev angry sunset with dis
d "\"Eu vou torná-los residentes PERMANENTES de Echo... e por residentes, quero dizer mortos!\""
c "\"Devon...\""
"Agora Devon pode perceber que o coyote realmente está chateado."
show dev surprised h sunset with dis
d "\"O que se passa, querido?\""
show cam sad sunset with dis
c "\"Disseste-me que ninguém vivia aqui. Disseste isso várias vezes.\""
show dev shocked h sunset with dis
d "\"Cameron, isso apareceu tão poucas vezes no fórum, e os posts que lembro eram tão banais. Honestamente, simplesmente esqueci.\""
show cam disappointed sunset with dis
c "\"Está bem.\""
"Devon olha para o coyote, esperando, mas ele não diz nada."
show dev surprised p sunset with dis
d "\"Cameron.{cps=3}..{/cps}{w=0.4} Há alguma coisa que queiras contar-me?{w=0.3} Se houver, ainda estou à espera que sejas aberto como disseste--\""
show cam frustrated sunset with dis
c "\"Ugh! {w=0.3}Eu sei.\""
show dev scared sunset with dis
d "\"Ei, está tudo bem, mano! Não estou à espera que agora compartilhes tudo o que tens em mente, mas estou aqui para ouvir se quiseres falar.\""
show cam sad sunset with dis
c "\"É só.{cps=3}..{/cps}{w=0.4} é difícil de explicar.\""
c "\"Acho que o facto de ainda haver pessoas reais a viver aqui torna tudo um pouco mais assustador.\""
show dev worried p sunset with dis
d "\"Tem a ver com os sonhos que estavas a ter?\""
"Dev observa Cameron atentamente, mas ele também parece genuinamente confuso."
show cam worried a sunset with dis
c "\"Mais ou menos, mas foram estranhos. Não acho que tenham realmente algum significado.\""
show cam smile sunset with dis
c "\"Sim, estou só a exagerar. Eu só não quero ter a experiência de {i}Deliverance{/i} além dos fantasmas, sabes?\""
show dev p sunset with dis
d "\"Eu entendo, e não há nada de errado em ser vigilante.\""
d "\"O meu amigo de Southland, aquele da cidade ainda mais assombrada que Echo--\""
d "\"--ele diz que algo horrível acontece entre um mochileiro e um redneck do Outback a cada dois anos, mais ou menos.\""
show cam serious c sunset with dis
c "\"Que reconfortante.\""
d "\"Mas, embora estivesse a brincar antes, se alguém tentar alguma coisa, eu {i}vou{/i} fazer o que for preciso para os parar.\""
"Dev não diz a Cameron que, naquele momento, ele até gostaria de ter ido em frente e comprado uma arma para proteção."
"Se esses homens ainda andam por aí, o urso não tem dúvidas de que têm muitas armas."
c "\"Bem, não vamos pensar nisso porque não vai acontecer.\""
show cam smirk c l sunset with dis
c "\"A menos que eles estejam a ocupar aquele quarto.\""
show dev angry sunset with dis
d "\"Não por muito tempo!\""
window hide
pause 0.5
stop background fadeout 5.0
play sound doorsqueak
scene bg motel_room_disarray with medium_dissolve
pause 1.0
window show
"O exagero de bravata de Devon transforma-se genuinamente em cautela ao abrir a porta."
"O quarto está mais quente do que lá fora, como se estivesse a amplificar e prender o calor."
show dev h dark3 at left with dissolve
play music roadsideintro fadein 3.0 volume 0.3
queue music roadsideloop volume 0.3
d "\"Ok.{cps=3}..{/cps}{w=0.4} Ok, {w=0.3}sim, {w=0.3}isto é viável.\""
d "\"Ei, Cam! {w=0.3}Tudo limpo!\""
show cam happy eyes dark3 at right with dissolve
c "\"Aww, sem hillbillies assassinos na--\""
show cam shocked dark3 at jumping
c "\"Oh, {w=0.3}nojo!\""
show dev surprised h dark3 with dis
d "\"O que esperavas? Só precisamos de arrumar um pouco. Olha, até há um colchão ali.\""
show cam scared dark3 with dis
c "\"Espera, não vamos usá-lo para dormir, ou algo assim, vamos?\""
show dev smirk p dark3 with dis
d "\"Porque é que achas que trouxe lençóis?\""
show cam disgusted dark3 with dis
c "\"Oh, eu NÃO vou dormir em--\""
d "\"Estou a brincar, estou a brincar. Esses são só para nos cobrir os lugares nojentos onde possamos sentar. Já te disse que tenho um quarto reservado em Payton.\""
c "\"E é melhor usá-lo, não importa o quanto te envolvas nisto.\""
show dev h dark3 with dis
d "\"Claro, mas podemos pelo menos tornar este lugar o mais confortável possível.\""
"Cameron está em silêncio e Devon vira-se para vê-lo a olhar fixamente para uma pilha de pregos enferrujados no chão à volta da janela e do colchão."
show cam serious c dark3 with dis
c "\"A tua vacina contra tétano está em dia, certo?\""
show dev surprised h dark3 with dis
d "\"Essa é uma excelente pergunta.\""
show cam disgusted dark3 with dis
stop music fadeout 7.0
c "\"Sim, ótimo. Só não te fures em nada. Vou tentar limpar isto, pelo menos, juntamente com todas as outras coisas afiadas e enferrujadas neste chão.\""
window hide
pause 0.5
scene black with medium_dissolve
play background crickets fadein 3.0
scene bg motel_room_night_light with medium_dissolve
pause 0.5
window show
"Cameron observa Devon dar um passo para trás, esfregando as patas uma na outra em alto som."
show dev p lamp at left with dissolve
d "\"Bem, eu diria que isto está bastante acolhedor, não achas?\""
show cam smile a lamp at right with dissolve
c "\"Já vi casas reais que parecem piores, então sim, eu diria que sim.\""
show cam worried a lamp with dis
"Cameron olha para o sofá e senta-se lentamente na beirada, não confiando totalmente nele, apesar do lençol."
show dev happy lamp with dis
d "\"Então! {w=0.4}O que sabes sobre investigação paranormal? Disseste que fizeste pesquisa?\""
show cam smile talking c lamp with dis
c "\"Acontece que só tens de correr por aí com uma lanterna e chamar o fantasma de vaca.\""
show dev serious h lamp with dis
d "\"Boa piada.\""
show cam grinning c lamp with dis
c "\"Merda, desculpa. Não sabia que as caçadas de fantasmas daqueles programas de reality show eram um assunto tão sensível para ti.\""
show dev worried p lamp with dis
d "\"Eles arruinaram completamente a credibilidade das investigações {i} reais {/i}.\""
show cam smile a lamp with dis
c "\"Bem, trouxeram mais atenção, certo? De qualquer forma, tudo o que realmente sei é o que tu fazes: coisas de EVP, tirar fotos, sentar e esperar. Coisas assim.\""
show dev h lamp with dis
d "\"Isso é um começo.\""
show cam surprised c lamp with dis
c "\"Na verdade, estava a pensar que tu tratarias da maioria dessas coisas, por isso o que eu pesquisei tinha a ver com aqueles que são... especiais.\""
"É quase fisicamente impossível para o coyote usar essa palavra para descrever pessoas como ele."
show dev grin h lamp with dis
d "\"Ah sim! Queria dizer-te antes o quanto fiquei contente por teres lido aquele fórum.\""
d "\"Deve ser chato ouvir-me a falar disso quando eu nem sequer o experimento.\""
show cam worried a lamp with dis
c "\"Não, estás bem, Dev.\""
"Na verdade, Cameron preferia ouvir isso de Devon."
"Metade das pessoas nos fóruns eram claramente mentirosas com um complexo de salvador--"
"--e a outra metade estava a contactar esses idiotas para tentar comunicar com um ente querido falecido."
"Cameron não aguentou isso e acabou por olhar para um blog que parecia um pouco mais legítimo."
show dev happy lamp with dis
d "\"Então, o que descobriste?\""
"A maneira como o urso está iluminado agora que estão a falar sobre investigação faz Cameron lembrar-se de que precisa pelo menos tentar."
show cam confused a lamp with dis
c "\"Bem, de acordo com esses médiuns, é bem simples se tivermos o sentido extra.\""
c "\"Primeiro, aproxima-te do local com intenções claras. Estou aqui para ver ou ouvir algo do passado.\""
c "\"Em segundo lugar, mantém uma mente aberta, o que prometo fazer.\""
show cam serious a l lamp with dis
c "\"E, finalmente, se sentires que a presença é hostil, lembra-te sempre que ela {i}pode{/i} magoar-te. Nestes casos, elas podem nunca ter sido realmente uma pessoa.\""
show dev annoyed p lamp with dis
d "\"Eh, eu não me preocuparia com coisas de demónios. Até eu tenho dificuldade em acreditar nisso.\""
show cam smile a l lamp with dis
c "\"Ei, há algo em que podemos concordar! Agora, vou arriscar e assumir que algo terrível aconteceu neste quarto?\""
show dev worried h lamp with dis
d "\"Umm...\""
show cam smile c l lamp with dis
c "\"Porque, senão, porque procurar um quarto específico, certo? Não quero que me digas o que aconteceu, mas também suponho que isto seja um teste, certo?\""
d "\"Bem, não quero chamar-lhe um teste. Vou estar a gravar e à procura... daquilo que aconteceu neste quarto também.\""
show dev surprised h lamp with dis
d "\"Só pensei que poderias querer ver se sentes alguma coisa e comparar com o que realmente aconteceu.\""
c "\"Acho que é uma boa ideia. Vou fazer algum 'toque leve', acho que chamam assim. Por isso, não vou ver nada, mas só sentir o que pode ter acontecido.\""
show dev confused talking p lamp with dis
d "\"Mas avisa-me se sentires que algo não está certo, claro.\""
show cam smile c l lamp with dis
c "\"Fico bem.\""
show dev happy eyes lamp with dis
d "\"Está bem, vou começar. Não vamos ficar até tarde esta noite. Só quero sentir o ambiente.\""
show cam surprised a lamp with dis
c "\"Claro. Eu vou... começar por abrir a minha mente e deixar as minhas intenções claras.\""
show dev grin h lamp with dis
d "\"Ok, querido. Amo-te.\""
hide cam
hide dev
with dissolve
"Devon inclina-se e beija Cameron na cabeça."
"Depois, Cameron observa enquanto Dev desliga a lanterna, mergulhando-os na escuridão."
window hide
pause 0.5
scene black with medium_dissolve
scene bg motel_room_night with medium_dissolve
pause 0.5
window show
"Carregar equipamento enquanto tenta ser silencioso faz Devon suar rapidamente através da sua camisa."
"Ele não tinha realmente pensado no calor, mesmo quando Cameron estava a queixar-se disso, mas a sua camisa estava colada ao seu pelo e teve de a tirar."
"Ele está a fazer um esforço extra para não incomodar o coyote, porque Cameron parece realmente estar a tentar, com os olhos fechados e as orelhas levantadas."
"Devon nem precisou pedir para ele tirar o telemóvel para poder gravar áudio."
"Ele simplesmente fez isso, e para Devon, isso apenas prova o quanto Cameron quer fazer isto."
"Enquanto Devon vai testando o seu equipamento, Cameron mexe-se e murmura algo."
"Dev alerta-se."
show dev surprised s dark at left with dissolve
d "\"Ei, amor, estou aqui. Estás bem?\""
c "\"Preciso de... estar mais confortável.\""
"Simultaneamente, ele ajusta-se para que os pés fiquem na mala à sua frente."
d "\"O--Ok...\""
show dev embarrassed s dark with dis
"Há algo no comportamento de Cameron que está a incomodar Devon."
"E as palavras de Cameron estavam ligeiramente arrastadas, e ele parece estar... não exatamente ali."
"Deveria ele tirá-lo disso?"
"Devon nunca tinha visto um psíquico em ação antes, por isso talvez isto seja normal, como um transe."
"Ele espera que seja normal, porque mesmo que Devon consiga encontrar as suas respostas, ele as entregaria para que Cameron descobrisse que não é \"psicótico\"."
"Enquanto mexe no seu sensor EMF, um pressentimento de angústia agarra-lhe o peito."
show dev disappointed s dark with dis
"E se o oposto acontecesse, e o Cam realmente perdesse a cabeça?"
"Como quando a mãe dele teve psicose?"
"SE isso acontecer, Devon só agora está a perceber que seria responsável, e como é que Cameron o perdoaria por isso?"
"Como é que ele se perdoaria a ele próprio?"
show dev frustrated s dark with dis
d "\"Merda...\""
"Dev sibila por entre os dentes."
"O que é que ele {i}está a fazer{/i}, a trazer o namorado para este quarto, onde {i}aquilo{/i} aconteceu?"
"Normalmente, ele estava sozinho, ou com amigos, quando fazia estas investigações, e a sua vontade de ver algo sobrepunha-se sempre ao medo."
"Ele simplesmente assumiu que o Cam estaria habituado a cenas assustadoras, especialmente depois de lhe ter descrito aquela criatura de cara lisa com um impermeável que via desde pequeno."
"Ele apenas assumiu."
show dev disappointed s dark with dis
"Porque é que só agora está a perceber as consequências que isto pode ter?"
"Bem, é porque as coisas que o Cameron lhe contou junto ao lago mudaram muita coisa na cabeça do urso."
"Isto não é algo que um parceiro amoroso faz a outro parceiro."
"Ele está a {i}usar{/i} o Cameron por razões egoístas."
"O Devon sabe que o coiote tem algum tipo de habilidade ESP, mas isso não quer dizer que não tenha outros problemas que o possam deixar ainda mais mal."
"Isso não quer dizer que ver estas coisas horríveis não lhe {i}cause{/i} ainda mais problemas."
hide dev with dissolve
stop background fadeout 5.0
"Todo o ânimo se esvai dele, e o Devon fixa o olhar no chão, a pensar."
"Depois levanta-se e começa a andar de um lado para o outro, a tomar uma decisão — logo depois disto, acabam, aconteça o que acontecer."
"O urso olha para o armário, aquele onde um lobo do conselho tribal da Meseta se enforcou no início dos anos 90."
"Se ao menos conseguisse ver uma coisa, apenas uma prova de que ela está bem do outro lado, ele ficaria em paz com tudo isto."
"Na verdade, o maior obstáculo é a vergonha de abandonar os seus planos e ter de explicar ao Cameron porquê."
"O Dev solta um suspiro trémulo, a olhar para dentro do armário, a observar aquela barra, a pensar se será a mesma que o lobo usou..."
play music2 looming volume 0
play music loomingintro fadein 10.0 volume 0.3
queue music loomingloop volume 0.3
"O Devon sente algo."
"Algo mau."
"Um arrepio percorre-lhe a espinha, e de repente está a tremer."
d "\"{cps=20}Não pode ser.\""
"Está.{cps=3}..{/cps}{w=0.5} Está mesmo a acontecer."
d "\"{cps=20}Foda-se... {w=0.5}Foda-se...\""
"É tudo o que consegue dizer."
"Está a acontecer, {w=0.4}mas sente-se tão.{cps=3}..{/cps}{w=0.4} {i}errado{/i}."
"Depois, é invadido por um medo que nunca conheceu antes."
"Quer virar-se."
"Quer chamar pelo Cameron, mas é como se algo o estivesse a agarrar pelo pescoço, impedindo-o de se mexer."
"E então ouve um som terrível atrás dele..."
window hide
pause 0.5
scene bg black with medium_dissolve
pause 0.5
window show
"O Cameron sabe que algo está a acontecer de certeza."
"É assustador, mas ao mesmo tempo, está a pôr em causa tudo em que sempre acreditou."
"Será que o Devon tinha razão sobre estas coisas?"
"Será que ele simplesmente se tinha interpretado mal durante todo este tempo?"
"Consegue sentir {i}alguém{/i}, nada como os monstros que tinha visto no passado."
"Em vez disso, era um homem, de fato e com um laço de couro."
"Ele estava triste, {w=0.5}estava zangado, {w=0.5}e estava aterrorizado."
"O Cameron sabia que era isto que os médiuns costumavam descrever quando falavam em \"sentir\" pessoas do passado."
"Sentes o momento mais intenso da vida delas, este homem, este lobo, vai fazer algo terrível."
"E enquanto o Cameron se maravilha com isto, o lobo de repente... muda."
"Ao mesmo tempo, o Cameron sente o foco virar-se para ele."
"Isto faz o coiote hesitar, porque agora esta presença está a tentar interagir com {i}ele{/i}."
"Isto será certo?"
"O Cameron acha que sim, mas algo não bate certo, como se isto não fosse o que ele pensa que é."
"Mas supõe que qualquer um a fazer isto pela primeira vez se sentiria estranho."
"Talvez estivesse a fazer mal a parte da “leitura”; o objetivo era ouvir o passado, como uma gravação."
"Esta comunicação direta está a assustar o coiote, mas esta pode ser a sua oportunidade para responder à pergunta do Dev — e à sua própria, já agora."
pause 1.0
centertext "{i}{cps=60}Desculpa incomodar. {w=0.6}O que acontece depois da morte?\n {w=0.4}Para onde vamos?{/i}"
pause 1.0
stop music2
stop music fadeout 5.0
play ambient wind2 fadein 3.0
"Sente-se estúpido e desajeitado, mas é tudo o que lhe vem à cabeça, então o Cameron pergunta vezes sem conta."
"Há uma longa pausa, vazia."
play sound cackle volume 0.4
"E depois, algo como uma gargalhada."
play sound2 cackle volume 0.4
"Quase parece falsa, como um brinquedo de Halloween, mas é sombria, cruel, e está a gozar com ele."
play sound cackleloud volume 0.4
"Todos os sentimentos de admiração e esperança por uma descoberta desvanecem-se num instante."
"Precisa do Dev, precisa de abrir os olhos..."
window hide
scene closet_blurry with medium_dissolve
pause 1.0
window show
"Os olhos do Cameron estão pesados, e mal consegue focar."
"Algo correu terrivelmente mal."
"Esta presença é maligna, {w=0.4}maliciosa, {w=0.4}isto não é uma pessoa."
"Agora, tudo o que o coiote consegue sentir é que acabou de acontecer uma tragédia profunda."
"Precisa do Devon, e acha que o vê à medida que a visão começa lentamente a focar-se."
window hide
pause 1.0
scene closet_1 with medium_dissolve
pause 1.0
play music2 closet volume 0
play music closetintro fadein 3.0 volume 0.3
queue music closetloop volume 0.3
pause 1.0
window show
".{cps=1}..{/cps}{w=1.0}{nw}"
"Primeiro, o Cameron não entende o que está a ver."
"Como é que o Dev está de pé daquela maneira?"
"Porque é que não se está a mexer?"
"Percebe porquê nos segundos seguintes."
"A forma antinatural como o peso do Dev parece puxar-lhe o pescoço para cima diz tudo."
"O Cameron começa a gritar, mas é fraco, abafado, quase um sopro da garganta... e não se consegue mexer."
"Paralisia."
"Isto não é real!"
"Isto é paralisia do sono... mas há algo nisto que é tão errado, tão real, e ele tem quase a certeza de que não adormeceu."
"Mas mesmo que tenha adormecido, o namorado pode mesmo estar a enforcar-se enquanto o coiote está ali, inútil, sentado no sofá."
"O terror começa a dominá-lo."
"Como é que isto aconteceu?"
stop music2
stop music fadeout 5.0
"Como é que ele pôde fazer isto!?"
scene closet_2 with dis
play background mobile
".{cps=1}..{/cps}{w=1.0}{nw}"
"Como?"
"O Cameron tenta gritar outra vez, mas de novo sai apenas um sopro."
"Fica a olhar para a imagem de contacto do Devon, em vez do Devon morto no armário."
"Tiraram aquela foto na universidade, há cinco anos, apenas um mês depois de começarem a namorar."
"Na altura, era uma recordação para mostrar aos outros amigos gays, para provar que tinha um namorado, e que era um urso jeitoso."
"E nunca a mudou, mesmo que já não tivesse ninguém a quem o mostrar."
"Como raio é que vieram aqui parar?"
scene closet_3 with dis
stop background
"O telefone atende automaticamente e muda para alta-voz."
"O Cameron sabe, lá no fundo, que isto deve ser um sonho, mas o Devon continua enforcado no armário."
"E é dominado pelo horror de que isto possa ser só um sonho parcial, e que a pior parte seja real."
"Isso faz o Cameron tentar, e falhar, gritar outra vez."
play background radiostatic fadein 3.0
unk "\”{cps=20}...Tu{w=0.3}...que--{w=0.4}rias saber...{w=0.5}como é?\""
"O Cameron olha para o telefone, sem conseguir perceber através do estático, mas reconhecendo a voz."
d "\"Disseste.{cps=4}..{/cps} {w=0.5}que querias saber como era.{cps=4}..{/cps} {w=0.5}morrer?\""
d "\"Eu diria.{cps=3}..{/cps}{w=0.4} que é como afogar-se para sempre.\""
d "\"Estar consciente para sempre enquanto sufocas por aquilo que te fazia feliz em vida.\""
d "\"Mas vá, {w=0.4}TU não acreditas em nada,{w=0.4} por isso o que queres mesmo saber é como é desaparecer.\""
d "\"Porque tens medo.\""
d "\"Dizes a ti próprio que queres morrer, que gostavas que a tua mãe não te tivesse salvo a vida miserável, que merecias isso.\""
d "\"Agora dizes a ti mesmo que se não fosse por mim, tinhas acabado com tudo na universidade.\""
d "\"Nós os dois sabemos que isso é mentira, porque és um cobarde do caraças.\""
d "\"Vais ficar vivo enquanto conseguires estar com alguém que te mantenha assim.\""
d "\"Eu podia ter-te tratado como uma merda nestes últimos cinco anos e tu ainda estarias aqui hoje.\""
d "\"Suplicaste ao Dylan que não te deixasse, só semanas depois dele te ter dado um murro e deixado essa cicatriz. Aquela que disseste que foi por caíres contra um armário. Estás doente.\""
d "\"Entretanto, tu {i}permitiste{/i} que eu te metesse nesta situação. Disseste que {i}querias{/i} isto. Ainda queres?\""
"{i}Não, {w=0.2}não, {w=0.2}não, {w=0.3}por favor Deus, {w=0.3}NÃO!{/i}"
"O Cameron nem sequer consegue mexer os lábios."
d "\"Enfim, já me estou a desviar um bocado, não é? Querias saber como é o pós-vida? Vou dar-te uma ideia.\""
"A voz do Devon fica mais abafada."
d "\"Yo, {w=0.3}Lupita! {w=0.3}Diz ao meu namorado como é.\""
stop background fadeout 5.0
"Fica tudo em silêncio por um momento, e o Cameron fica ali sentado, numa miséria atónita, só à espera."
play sound staticscream
stop ambient
show bs
"Um grito terrível e demoníaco atravessa o telefone e o pelo do Cameron arrepia-se todo, enquanto luta contra esta prisão com tudo o que tem." with vpunch
"E finalmente liberta-se."
window hide
#ADD AMBIENCE?
pause 1.0
scene bg motel_room_night with medium_dissolve:
    zoom 1.02
    xalign 0.5
    yalign 0.5
pause 1.0
window show
"It takes Devon a moment to realize the terrible sound is coming from Cameron."
"Nunca ouviu o Cameron fazer um som daqueles."
"Naquele momento, seja o que for que está a agarrar o urso, desfaz-se, e o Devon vira-se, ofegante."
"Quando o Dev olha para ele, vê os olhos do Cameron arregalados."
show dev scared s dark at left with dissolve
d "\"Cameron!?\""
"O Cameron volta a fazer aquele som."
"Embora o Devon não faça ideia do que o Cameron está a ver, sabe que é algo terrível."
"O Devon sente o pânico a instalar-se."
show dev angry s dark with dis
d "\"Amor, {w=0.3}por favor! {w=0.4}O que está a acontecer!?\""
"O Cameron apenas o encara, e o Devon perde o controlo."
show dev angry yelling s dark
show cam horror dark at right
d "\"CAMERON!\"" with vpunch
"O Devon está a sair do armário quando, de repente, o Cameron salta do sofá, soltando um som selvagem."
play music2 solace volume 0
play music solaceintro fadein 10.0 volume 0.3
queue music solaceloop volume 0.3
"O olhar nos olhos do coiote é tão intensamente estranho que o Devon recua, assustado."
show dev scared s dark with dis
d "\"Querido, {w=0.3}sou eu!\""
window hide None
hide dev
hide cam
play sound thud5
with vpunch
pause 0.5
window show
"Para choque do Dev, as patas do Cameron vão para o pescoço do urso, mas em vez de apertarem como ele pensa, começam a puxar com força o pelo espesso."
show dev scared s dark at left with dissolve
d "\"Espera! {w=0.3}Para!\""
"O Devon consegue agarrar as patas do Cameron com as suas, muito maiores, imobilizando facilmente o macho mais pequeno."
show cam horror dark at right with dissolve
"O Cameron continua a olhar fixamente para o pescoço do Devon, como se procurasse algo com muita atenção, depois olha para o rosto dele."
show cam terror dark with dis
c "\"Vi-te morto. Ligaste-me e gritaste comigo.\""
"Embora o Devon não compreenda, percebe que isto não foi um dos terrores noturnos típicos do Cameron."
"A expressão no rosto dele diz tudo."
show dev frustrated s dark with dis
d "\"Foda-se!\""
show dev tears s dark with dis
d "\"Desculpa, desculpa mesmo. Vou levar-te a Payton agora, ou para onde quiseres.\""
"Mas quando o Devon tenta puxá-lo para a porta, o Cameron resiste."
show cam horror dark with dis
c "\"Espera, {w=0.3}espera. {w=0.5}Deixa-me só recuperar o fôlego, {w=0.3}sim?\""
d "\"Está bem, está bem. Respira fundo, sim?\""
show cam crying dark:
    choice:
        pause 0.1
    choice:
        easeout_back 0.1 xoffset -5
        easein_bounce 0.1 xoffset 0
    choice:
        pass
    pause 0.5
    repeat
with dis
hide dev with dis
"O Devon tenta acender o candeeiro até finalmente o conseguir ligar."
window hide
pause 0.5
scene motel_room_night_light:
    zoom 1.02
    xalign 0.5
    yalign 0.5
show cam crying lamp at right:
    yalign 0.0
    choice:
        pause 0.1
    choice:
        easeout_back 0.1 xoffset -5
        easein_bounce 0.1 xoffset 0
    choice:
        pass
    pause 0.5
    repeat
with dis
pause 1.0
show dev disappointed s lamp at left behind cam with dis
pause 0.5
window show
"Depois fica ao lado do Cameron durante alguns momentos, a ouvi-lo soluçar."
show dev embarrassed s lamp with dis
d "\"Posso, pelo menos, abraçar-te.{cps=3}..{/cps}{w=0.4} por favor?\""
hide cam with dissolve
show cam crying lamp at center:
    yalign 0.0
    choice:
        pause 0.1
    choice:
        easeout_back 0.1 xoffset -5
        easein_bounce 0.1 xoffset 0
    choice:
        pass
    pause 0.5
    repeat
with dis
"O Cameron inclina-se para ele como resposta."
"Enquanto o Dev lhe faz festas na cabeça, o Cameron começa a acariciar-lhe as costas, como se soubesse que o Dev também esteve apavorado."
show cam heartbreak lamp at center with dis
c "\"Estou bem. {w=0.5}Foi só uma visão mesmo intensa.{cps=3}..{/cps}{w=0.3}\""
show dev disappointed s lamp with dis
d "\"Desculpa tanto. Nunca te vi assim antes. Assustaste-me imenso.\""
d "\"Pensaste que eu.{cps=3}..{/cps}{w=0.4} Pensaste que te estava a atacar?\""
c "\"Hã?\""
d "\"Estavas a ir para o meu pescoço, mais ou menos.\""
c "\"Ah, não, eu, hum, vi-te enforcado no armário--\""
show cam crying lamp with dis
"A respiração do Cameron prende-se no peito."
c "\"Tipo, pelo pescoço.\""
show dev surprised s lamp with dis
d "\"Oh merda...\""
c "\"Yeah, e foi tão fodidamente real.\""
show dev embarrassed s lamp with dis
"Ficam abraçados em silêncio durante algum tempo, enquanto o Devon reflete sobre o que o Cameron acabou de lhe contar."
show dev disappointed s lamp with dis
"O Devon já não tem dúvidas de que o Cameron é médium, mas neste momento isso não importa."
"Só quer que o coiote se sinta seguro outra vez."
show cam heartbreak lamp with dis
c "\"Devon?\""
show dev embarrassed s lamp with dis
d "\"Sim, querido?\""
c "\"Acho que tinhas razão.\""
d "\"Sobre o quê?\""
c "\"Aconteceu alguma coisa. Não sei se foram fantasmas ou--ou o que raio foi aquilo, mas não fui só eu.\""
c "\"Nunca senti ou vi coisas assim antes. Há mais nisto do que eu estar maluco.\""
c "\"Tem de haver...\""
show dev smirk h s lamp with dis
d "\"Podemos falar sobre isso quando estivermos em Payton, está bem?\""
show cam terror lamp with dis
stop music2
stop music fadeout 10.0
c "\"Dev, prometi ser honesto contigo, e tenho de te dizer isto agora, senão provavelmente nunca vou conseguir.\""
show dev surprised s lamp with dis
d "\"O que foi?\""
"O coração do Dev começa a acelerar ao ver a expressão do Cameron."
show cam heartbreak lamp with dis
c "\"A Lupita apareceu nesta visão, Dev... Mas por favor acredita que não acho que fosse mesmo ela, mas...\""
show dev scared s lamp with dis
d "\"O quê!?\""
"O Cameron hesita."
show dev surprised s lamp at left with dis
d "\"Cameron, {w=0.3}{i}por favor{/i}, diz-me.\""
show cam crying lamp with dis
c "\"Desculpa mesmo, mas ouvi-a, e foi horrível e... não sei, foi só um grito. Foi horrível.\""
scene black
show dev surprised s dark4 at left
with dis6
"O chão parece desaparecer debaixo dos pés do Devon, e sente que está a cair num abismo."
window hide
pause 1.0

jump a1s2
