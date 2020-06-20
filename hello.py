#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return """
        <!DOCTYPE html>
<html lang="en">
<title>Formulario</title>
</head>
<!--MANDAMOS A TRAER PURE CSS-->
<link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css">
<meta name="viewport" content="width=device-width, initial-scale=1">

<meta charset="utf-8">
</head>
<center>
<form class="pure-form pure-form-aligned">
    <div class="inputBox">
        <h1>FORMULARIO</h1>
    <fieldset>
        <div class="pure-control-group">
            <label for="aligned-name">Matricula</label>
            <input type="number" id="aligned-number" placeholder="Ingresa Matricula" />
        </div>
        <div class="pure-control-group">
            <label for="aligned-name">Nombre</label>
            <input type="text" id="aligned-name" placeholder="Ingresa nombre" />
        </div>
        <div class="pure-control-group">
            <label for="aligned-apepate">A.Paterno</label>
            <input type="text" id="aligned-apepate" placeholder="Ingresa apellido" />
        </div>
        <div class="pure-control-group">
            <label for="aligned-apemate">A.materno</label>
            <input type="text" id="aligned-apemate" placeholder="Ingresa apellido" />
        </div>
        <div class="pure-control-group">
            <label for="stacked-state">Edad</label>
            <select id="stacked-state">
                <option>Elige</option>
                <option>12</option>
                <option>13</option>
                <option>14</option>
                <option>15</option>
                <option>16</option>
                <option>17</option>
                <option>18</option>
                <option>19</option>
                <option>20</option>
                <option>21</option>
                <option>22</option>
                <option>23</option>
                <option>24</option>
            </select>  años
        </div>
        <div class="pure-control-group">
            <label for="stacked-state">Fecha de Nacimiento</label>
            <input type="date" id="party" min="1975-01-01" max="2050-01-01" required>
            <span class="validity"></span>
        </div>
        <div class="pure-control-group">
            <label for="stacked-state">Sexo</label>
                <input type="radio" id="checkbox-radio-option-two" name="optionsRadios" value="option1" checked="" />Femenino</label>
                <input type="radio" id="checkbox-radio-option-two" name="optionsRadios" value="option1" checked="" />Masculino</label>
        </div>
        <div class="pure-control-group">
            <label for="stacked-state">Estado</label>
            <select id="stacked-state">
                <option>Elige</option>
                <option>Soltero</option>
                <option>Casado</option>
            </select>
        </div>
        <div class="pure-controls">
            <label for="aligned-cb" class="pure-checkbox">
            <button type="submit" class="pure-button pure-button-primary">Guardar</button>
        </div>
    </div>
    </fieldset>
</form>
</center>
</html>
        """
    
    @cherrypy.expose
    def greet(self, name):
        return 'Hello {}!'.format(name)


cherrypy.config.update({'server.socket_port': 8090,
                        'engine.autoreload.on': False,
                        'log.access_file': './access.log',
                        'log.error_file': './error.log'})
cherrypy.quickstart(Root())