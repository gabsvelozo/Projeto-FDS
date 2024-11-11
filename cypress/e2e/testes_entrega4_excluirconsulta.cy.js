describe('Excluindo consultas',()=> {
    beforeEach(() => {
        cy.visit('/');
        cy.get('#username').type('gabi')
        cy.wait(100)

        cy.get('#password').type('gabi')
        cy.wait(100)

        cy.get('.bg-blue-500').click()
        cy.wait(100)
    });
    

    it('Marcando e desmarcando consulta', ()=> {
        cy.visit('/agendamento/');

        cy.get('#data').type('2024-11-11');
        cy.wait(1000)


        cy.get('div.px-4 > .w-full').click()
        cy.wait(1000)


        cy.get(':nth-child(3) > .block').click()
        cy.wait(1000)
        cy.get('.text-red-500').last().should('be.visible').click()
        cy.wait(1000)
        cy.get('.bg-red-500').should('be.visible')


        

        
    })
})