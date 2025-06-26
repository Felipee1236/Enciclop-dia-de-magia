-- Script para criação do banco de dados Enciclopédia de Magias
-- Execute este script no MySQL para criar o banco e as tabelas

CREATE SCHEMA IF NOT EXISTS `enciclopediaMagias` DEFAULT CHARACTER SET utf8;
USE `enciclopediaMagias`;

-- Tabela Escritor (necessária para a FK em Magia)
CREATE TABLE IF NOT EXISTS `enciclopediaMagias`.`Escritor` (
  `idEscritor` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idEscritor`)
);

-- Tabela Classe
CREATE TABLE IF NOT EXISTS `enciclopediaMagias`.`Classe` (
  `idClasse` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idClasse`)
);

-- Tabela Magia
CREATE TABLE IF NOT EXISTS `enciclopediaMagias`.`Magia` (
  `idMagia` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Nivel` INT CHECK (Nivel BETWEEN 0 AND 9),
  `Alcance` VARCHAR(45) NOT NULL,
  `Duracao` VARCHAR(45) NOT NULL,
  `Concentracao` BOOLEAN NOT NULL,
  `Escola` VARCHAR(45) NOT NULL,
  `Ritual` BOOLEAN NOT NULL,
  `Descricao` TEXT,
  `Escritor_idEscritor` INT NOT NULL,
  PRIMARY KEY (`idMagia`),
  FOREIGN KEY (`Escritor_idEscritor`)
    REFERENCES `Escritor` (`idEscritor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- Tabela de relacionamento Magia-Classe
CREATE TABLE IF NOT EXISTS `enciclopediaMagias`.`Magia_has_Classe` (
  `Magia_idMagia` INT NOT NULL,
  `Classe_idClasse` INT NOT NULL,
  PRIMARY KEY (`Magia_idMagia`, `Classe_idClasse`),
  FOREIGN KEY (`Magia_idMagia`)
    REFERENCES `Magia` (`idMagia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (`Classe_idClasse`)
    REFERENCES `Classe` (`idClasse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- Inserindo escritores
INSERT INTO Escritor (Nome) VALUES 
('Wizards of the Coast'),
('Dave Arcanista'),
('Cinnabar Místico');

-- Inserindo classes
INSERT INTO Classe (Nome) VALUES 
('Mago'), ('Bruxo'), ('Druida'), 
('Clérigo'), ('Bardo'), ('Paladino');

-- Inserindo magias
INSERT INTO Magia (Nome, Nivel, Alcance, Duracao, Concentracao, Escola, Ritual, Descricao, Escritor_idEscritor) VALUES
('Mãos Mágicas', 0, '30 pés', '1 minuto', FALSE, 'Conjuração', FALSE, 'Cria uma mão espectral que pode manipular objetos', 1),
('Raio de Gelo', 0, '60 pés', 'Instantâneo', FALSE, 'Evocação', FALSE, 'Um raio de energia congelante atinge o alvo', 1),
('Detectar Magia', 1, '30 pés', '10 minutos', TRUE, 'Divinação', TRUE, 'Permite detectar magias ativas na área', 1),
('Disfarce', 1, 'Pessoal', '1 hora', FALSE, 'Ilusão', FALSE, 'Altera sua aparência física', 1),
('Bola de Fogo', 3, '150 pés', 'Instantâneo', FALSE, 'Evocação', FALSE, 'Explosão de fogo que causa 8d6 de dano', 1),
('Invisibilidade', 2, 'Toque', '1 hora', TRUE, 'Ilusão', FALSE, 'Torna uma criatura invisível', 1),
('Teletransporte', 5, '10 pés', 'Instantâneo', FALSE, 'Conjuração', FALSE, 'Transporta você e outros para local conhecido', 1),
('Proteção Contra Energia', 3, 'Toque', '1 hora', TRUE, 'Abjuração', FALSE, 'Protege contra um tipo de dano específico', 1),
('Muralha de Gelo', 4, '120 pés', '10 minutos', TRUE, 'Evocação', FALSE, 'Cria uma muralha de gelo', 1),
('Ressurreição', 7, 'Toque', 'Instantâneo', FALSE, 'Necromancia', FALSE, 'Restaura vida a uma criatura morta', 1);

-- Associando magias a classes
INSERT INTO Magia_has_Classe (Magia_idMagia, Classe_idClasse) VALUES
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),  -- Mãos Mágicas para várias classes
(2, 1), (2, 2), (2, 3),                    -- Raio de Gelo
(3, 1), (3, 2), (3, 3), (3, 4), (3, 5),    -- Detectar Magia
(4, 1), (4, 2), (4, 5),                    -- Disfarce
(5, 1), (5, 2),                             -- Bola de Fogo
(6, 1), (6, 2), (6, 5),                    -- Invisibilidade
(7, 1), (7, 2),                             -- Teletransporte
(8, 1), (8, 3), (8, 4), (8, 6),            -- Proteção Contra Energia
(9, 1), (9, 3),                             -- Muralha de Gelo
(10, 2), (10, 4), (10, 6);                 -- Ressurreição

-- Consultas de exemplo para testar o banco
SELECT 'Banco de dados criado com sucesso!' as Status;

