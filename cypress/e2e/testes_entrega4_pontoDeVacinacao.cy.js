describe('pontos de vacinação da região',()=> {
    beforeEach(() => {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.wait(100)

        cy.get('#password').type('gabi')
        cy.wait(100)

        cy.get('.bg-blue-500').click()
        cy.wait(100)
    });
    it('Vacinas em Boa Viagem', ()=> {
        cy.visit('/vacinas/');
        cy.wait(1000)

        cy.get('#bairro-select').select('Boa Viagem')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)

        cy.get('.tela > .text-xl').invoke('text').should('have.string', "Shopping Recife")
        cy.wait(1000)

    })
    
    it('Vacinas em Boa Viagem', ()=> {
        cy.visit('/vacinas/');
        cy.wait(1000)

        cy.get('#bairro-select').select('Santo Amaro')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)
        
        cy.get(':nth-child(2) > .text-xl').invoke('text').should('have.string', "Shopping Tacaruna")
        cy.wait(1000)

        cy.get(':nth-child(3) > .text-xl').invoke('text').should('have.string', "Policlínica Waldemar de Oliveira")
        cy.wait(1000)

        cy.get(':nth-child(4) > .text-xl').invoke('text').should('have.string', "USF Ilha Sta. Terezinha")
        cy.wait(1000)


    })

    it('Vacinas em Boa Viagem e Santo Amaro', ()=> {
        cy.visit('/vacinas/');
        cy.wait(1000)

        cy.get('#bairro-select').select('Boa Viagem')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)

        cy.get('.tela > .text-xl').invoke('text').should('have.string', "Shopping Recife")
        cy.wait(1000)

        cy.get('#bairro-select').select('Santo Amaro')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)
        
        cy.get(':nth-child(2) > .text-xl').invoke('text').should('have.string', "Shopping Tacaruna")
        cy.wait(1000)

        cy.get(':nth-child(3) > .text-xl').invoke('text').should('have.string', "Policlínica Waldemar de Oliveira")
        cy.wait(1000)

        cy.get(':nth-child(4) > .text-xl').invoke('text').should('have.string', "USF Ilha Sta. Terezinha")
        cy.wait(1000)


    })
})