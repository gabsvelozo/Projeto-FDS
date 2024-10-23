describe('agendamento de consultas',()=> {
    it('agendamento de consultas de forma certa', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.get('#password').type('gabi')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(2) > .block').click()
        cy.get('#especialidade').select('Ginecologia')
        cy.get('#local').select('UPAE-R')
        cy.get('#data').click()
        cy.get('.px-4 > .w-full').click()
    })  
    it('entrado em agendamento sem enviar nada', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.get('#password').type('gabi')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(2) > .block').click()
        cy.get('.ml-2').click()
    })
    it('entrado em consultas pelo agendamento', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.get('#password').type('gabi')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(2) > .block').click()
        cy.get('.ml-10 > [href="/consultas/"]').click()
    })
})

describe('ver minhas consultas',()=> {
    it('ver as consultas', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.get('#password').type('gabi')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(3) > .block').click()
        cy.get('.border-b > :nth-child(1)')
        cy.get('.border-b > :nth-child(2)')
        cy.get('.border-b > :nth-child(3)')
        cy.get('div.items-center > :nth-child(2) > .text-xl').click()
    })  
    it('saindo de consultas e entrando em agendamentos', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.get('#password').type('gabi')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(3) > .block').click()
        cy.get('.border-b > :nth-child(1)')
        cy.get('.border-b > :nth-child(2)')
        cy.get('.border-b > :nth-child(3)')
        cy.get('.ml-10 > [href="/agendamento/"]').click()
    })
    it('visualizando as consultas', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.get('#password').type('gabi')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(3) > .block').click()
        cy.get('.border-b > :nth-child(1)')
        cy.get('.border-b > :nth-child(2)')
        cy.get('.border-b > :nth-child(3)')
        cy.get('div.items-center > :nth-child(2) > .text-xl').click()
    })
})

describe('localização',()=> {
    it('escolhendo o local', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.get('#password').type('gabi')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(6) > .block').click()
        cy.get('#bairro-select').select('Boa Viagem')
        cy.get('div.px-4 > .w-full').click()
        cy.get(':nth-child(2) > .text-xl')
        cy.get('#informacoes > :nth-child(2) > :nth-child(3)')
    })  
    it('saindo pela barra embaixo', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.get('#password').type('gabi')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(6) > .block').click()
        cy.get('#bairro-select').select('Casa Amarela')
        cy.get('div.px-4 > .w-full').click()
        cy.get(':nth-child(2) > .text-xl')
        cy.get('#informacoes > :nth-child(2) > :nth-child(3)')
        cy.get('.text-blue-500').click()
    })
    it('usando pela nav bar', ()=> {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.get('#password').type('gabi')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(6) > .block').click()
        cy.get('#bairro-select').select('Estância')
        cy.get('div.px-4 > .w-full').click()
        cy.get(':nth-child(2) > .text-xl')
        cy.get('#informacoes > :nth-child(2) > :nth-child(3)')
        cy.get('.ml-2').click()
    })
})