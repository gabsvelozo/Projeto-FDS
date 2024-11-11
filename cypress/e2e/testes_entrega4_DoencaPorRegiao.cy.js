describe('Doenças por região',()=> {
    beforeEach(() => {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.wait(100)

        cy.get('#password').type('gabi')
        cy.wait(100)

        cy.get('.bg-blue-500').click()
        cy.wait(100)
    });
    it('Doenças em Boa Viagem', ()=> {
        cy.visit('/localizar_doencas/');

        cy.get('#bairro-select').select('Boa Viagem')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)

        cy.get('#informacoes > :nth-child(2)').invoke('text').should('have.string', "Febre Amarela")
        cy.wait(1000)

        cy.get('#informacoes > :nth-child(3)').invoke('text').should('have.string', "Salmonela")
        cy.wait(1000)
    })

    it('Doenças na Madalena', ()=> {
        cy.visit('/localizar_doencas/');

        cy.get('#bairro-select').select('Madalena')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)

        cy.get('#informacoes > :nth-child(2)').invoke('text').should('have.string', "Zikavírus")
        cy.wait(1000)
    })

    it('Doenças na Madalena', ()=> {
        cy.visit('/localizar_doencas/');

        cy.get('#bairro-select').select('Madalena')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)

        cy.get('#informacoes > :nth-child(2)').invoke('text').should('have.string', "Zikavírus")
        cy.wait(1000)
    })

    it('Doenças na Madalena e em Boa Viagem', ()=> {
        cy.visit('/localizar_doencas/');

        cy.get('#bairro-select').select('Madalena')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)

        cy.get('#informacoes > :nth-child(2)').invoke('text').should('have.string', "Zikavírus")
        cy.wait(1000)

        cy.get('#bairro-select').select('Boa Viagem')
        cy.wait(1000)

        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)

        cy.get('#informacoes > :nth-child(2)').invoke('text').should('have.string', "Febre Amarela")
        cy.wait(1000)

        cy.get('#informacoes > :nth-child(3)').invoke('text').should('have.string', "Salmonela")
        cy.wait(1000)
    
    })
})