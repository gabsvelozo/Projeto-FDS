describe('cadastro e login',()=> {
    it('histórico com todas as informações', ()=> {
        cy.visit('/');
        cy.get('#username').type('luis')
        cy.get('#password').type('1234')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(1) > .block').click()
        cy.get('#nome').type('luis')
        cy.get('#idade').type('18')
        cy.get('#medicacao').type('paracetamol')
        cy.get('#doencas').type('diabetes')
        cy.get('#cirugias').type('rinoplastia')
        cy.get('#alergias').type('amendoim')
        cy.get('.bg-blue-500').click()
    })  
    it('histórico com duas variaveis', ()=> {
        cy.visit('/');
        cy.get('#username').type('luis')
        cy.get('#password').type('1234')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(1) > .block').click()
        cy.get('#nome').type('luis eduardo')
        cy.get('#idade').type('20')
        cy.get('#medicacao').type('paracetamol e vitamina D')
        cy.get('#doencas').type('hipertensão e diabetes')
        cy.get('#cirugias').type('lipoaspiração e hernia de disco')
        cy.get('#alergias').type('acaro e leite')
        cy.get('.bg-blue-500').click()
    }) 
    it('historico sem nome', ()=> {
        cy.visit('/');
        cy.get('#username').type('luis')
        cy.get('#password').type('1234')
        cy.get('.bg-blue-500').click()
        cy.get(':nth-child(1) > .block').click()
        cy.get('#nome').should('have.value', '').then(() => {
            throw new Error('O campo não deve estar vazio, teste falhou!');
          });
        cy.get('#idade').type('20')
        cy.get('#medicacao').type('paracetamol e vitamina D')
        cy.get('#doencas').type('hipertensão e diabetes')
        cy.get('#cirugias').type('lipoaspiração e hernia de disco')
        cy.get('#alergias').type('acaro e leite')
        cy.get('.bg-blue-500').click()
    }) 

})