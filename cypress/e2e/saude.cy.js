describe('agendamento de consultas',()=> {
    beforeEach(() => {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.wait(100)

        cy.get('#password').type('gabi')
        cy.wait(100)

        cy.get('.bg-blue-500').click()
        cy.wait(100)
    });
    it('agendamento de consultas de forma certa', ()=> {
        cy.visit('/');


        cy.get(':nth-child(2) > .block').click()
        cy.wait(1000)

        cy.get('#especialidade').select('Ginecologia')
        cy.wait(1000)

        cy.get('#local').select('UPAE-R')
        cy.wait(1000)

        cy.get('#data').click()
        cy.wait(1000)

        cy.get('.px-4 > .w-full').click()
        cy.wait(1000)
    })  
    it('entrado em agendamento sem enviar nada', ()=> {
        cy.visit('/');
        cy.wait(1000)
        cy.get('#username').type('gabi')
        cy.wait(1000)
        cy.get('#password').type('gabi')
        cy.wait(1000)
        cy.get('.bg-blue-500').click()
        cy.wait(1000)

        cy.get(':nth-child(2) > .block').click()
        cy.wait(1000)

        cy.get('.ml-2').click()
        cy.wait(1000)

    })
    it('entrado em consultas pelo agendamento', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.wait(1000)

        cy.get('#password').type('gabi')
        cy.wait(1000)
        
        cy.get('.bg-blue-500').click()
        cy.wait(1000)

        cy.get(':nth-child(2) > .block').click()
        cy.wait(1000)

        cy.get('.ml-10 > [href="/consultas/"]').click()
        cy.wait(1000)

    })
})

describe('ver minhas consultas',()=> {
    it('ver as consultas', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.wait(1000)

        cy.get('#password').type('gabi')
        cy.wait(1000)

        cy.get('.bg-blue-500').click()
        cy.wait(1000)

        cy.get(':nth-child(3) > .block').click()
        cy.wait(1000)

        cy.get('.border-b > :nth-child(1)')
        cy.wait(1000)

        cy.get('.border-b > :nth-child(2)')
        cy.wait(1000)

        cy.get('.border-b > :nth-child(3)')
        cy.wait(1000)

        cy.get('div.items-center > :nth-child(2) > .text-xl').click()
        cy.wait(1000)

    })  
    it('saindo de consultas e entrando em agendamentos', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.wait(1000)

        cy.get('#password').type('gabi')
        cy.wait(1000)

        cy.get('.bg-blue-500').click()
        cy.wait(1000)

        cy.get(':nth-child(3) > .block').click()
        cy.wait(1000)

        cy.get('.border-b > :nth-child(1)')
        cy.wait(1000)

        cy.get('.border-b > :nth-child(2)')
        cy.wait(1000)

        cy.get('.border-b > :nth-child(3)')
        cy.wait(1000)

        cy.get('.ml-10 > [href="/agendamento/"]').click()
        cy.wait(1000)

    })
    it('visualizando as consultas', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.wait(1000)

        cy.get('#password').type('gabi')
        cy.wait(1000)

        cy.get('.bg-blue-500').click()
        cy.wait(1000)

        cy.get(':nth-child(3) > .block').click()
        cy.wait(1000)

        cy.get('.border-b > :nth-child(1)')
        cy.wait(1000)

        cy.get('.border-b > :nth-child(2)')
        cy.wait(1000)

        cy.get('.border-b > :nth-child(3)')
        cy.wait(1000)

        cy.get('div.items-center > :nth-child(2) > .text-xl').click()
        cy.wait(1000)

    })
})

describe('localização',()=> {
    it('escolhendo o local', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.wait(1000)

        cy.get('#password').type('gabi')
        cy.wait(1000)

        cy.get('.bg-blue-500').click()
        cy.wait(1000)

        cy.get(':nth-child(6) > .block').click()
        cy.wait(1000)

        cy.get('#bairro-select').select('Boa Viagem')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)

        cy.get(':nth-child(2) > .text-xl')
        cy.wait(1000)

        cy.get('#informacoes > :nth-child(2) > :nth-child(3)')
        cy.wait(1000)

    })  
    it('saindo pela barra embaixo', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.wait(1000)

        cy.get('#password').type('gabi')
        cy.wait(1000)

        cy.get('.bg-blue-500').click()
        cy.wait(1000)

        cy.get(':nth-child(6) > .block').click()
        cy.wait(1000)

        cy.get('#bairro-select').select('Casa Amarela')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)

        cy.get(':nth-child(2) > .text-xl')
        cy.wait(1000)

        cy.get('#informacoes > :nth-child(2) > :nth-child(3)')
        cy.wait(1000)

        cy.get('.text-blue-500').click()
        cy.wait(1000)

    })
    it('usando pela nav bar', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.wait(1000)

        cy.get('#password').type('gabi')
        cy.wait(1000)

        cy.get('.bg-blue-500').click()
        cy.wait(1000)

        cy.get(':nth-child(6) > .block').click()
        cy.wait(1000)

        cy.get('#bairro-select').select('Estância')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)

        cy.get(':nth-child(2) > .text-xl')
        cy.wait(1000)

        cy.get('#informacoes > :nth-child(2) > :nth-child(3)')
        cy.wait(1000)

        cy.get('.ml-2').click()
        cy.wait(1000)

    })
})