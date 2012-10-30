class TodosController < ApplicationController

	def index
		@todo = Todo.new
		@todos = Todo.where(:done => false)
	end

	def create
		@todo = Todo.create(params[:todo])
		respond_to do |format|
			format.html { redirect_to :root }
			format.js
		end
	end

	def finished

		@todo = Todo.find_by_id(params[:id].to_i)
		@todo.done = true
		@todo.save

		respond_to do |format|
			format.html { redirect_to :root }
			format.js
		end
	end
end
